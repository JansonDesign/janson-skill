#!/usr/bin/env python3
"""Normalize a height map to 8-bit grayscale PNG and report range metrics."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from PIL import Image


def percentile_from_histogram(histogram: list[int], total: int, percentile: float) -> int:
    target = math.ceil(total * percentile)
    running = 0
    for value, count in enumerate(histogram):
        running += count
        if running >= target:
            return value
    return 255


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--base-threshold", type=int, default=8)
    args = parser.parse_args()

    image = Image.open(args.input).convert("L")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        image.save(args.output, format="PNG", optimize=True)

    histogram = image.histogram()
    threshold = max(0, min(254, args.base_threshold))
    subject_histogram = histogram[:]
    for value in range(threshold + 1):
        subject_histogram[value] = 0
    subject_count = sum(subject_histogram)
    pixel_count = image.width * image.height

    weighted_sum = sum(value * count for value, count in enumerate(subject_histogram))
    mean = weighted_sum / subject_count if subject_count else 0.0
    variance = (
        sum(((value - mean) ** 2) * count for value, count in enumerate(subject_histogram))
        / subject_count
        if subject_count
        else 0.0
    )

    pixels = image.load()
    border_values = [
        *(pixels[x, 0] for x in range(image.width)),
        *(pixels[x, image.height - 1] for x in range(image.width)),
        *(pixels[0, y] for y in range(image.height)),
        *(pixels[image.width - 1, y] for y in range(image.height)),
    ]

    metrics = {
        "mode": image.mode,
        "size": [image.width, image.height],
        "base_threshold": threshold,
        "border_max": max(border_values) if border_values else 0,
        "black_base_fraction": sum(histogram[: threshold + 1]) / pixel_count,
        "subject_fraction": subject_count / pixel_count,
        "subject_mean": mean,
        "subject_std": math.sqrt(variance),
        "subject_p95": percentile_from_histogram(subject_histogram, subject_count, 0.95)
        if subject_count
        else 0,
        "subject_near_white_fraction": sum(subject_histogram[240:]) / subject_count
        if subject_count
        else 0.0,
    }
    print(json.dumps(metrics, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
