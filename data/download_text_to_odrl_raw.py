#!/usr/bin/env python3
"""Download a Hugging Face dataset as raw JSONL and input-only text files.

This downloader uses the public Hugging Face dataset-server API, so it does
not require pyarrow, pandas Parquet support, or the ``datasets`` package.
"""

from __future__ import annotations

import argparse
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


DEFAULT_DATASET = "Yusra2677/text-to-odrl-dataset-v1"
DEFAULT_SPLITS = ("train", "validation", "test")
ROWS_ENDPOINT = "https://datasets-server.huggingface.co/rows"


def _request_page(
    dataset: str,
    split: str,
    offset: int,
    page_size: int,
    timeout: int,
    attempts: int = 4,
) -> Dict[str, object]:
    query = urlencode(
        {
            "dataset": dataset,
            "config": "default",
            "split": split,
            "offset": offset,
            "length": page_size,
        }
    )
    request = Request(
        f"{ROWS_ENDPOINT}?{query}",
        headers={"User-Agent": "odrl-extraction-dataset-downloader/1.0"},
    )
    for attempt in range(1, attempts + 1):
        try:
            with urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
            if attempt == attempts:
                raise
            time.sleep(min(2**attempt, 10))
    raise RuntimeError("unreachable")


def _normalise_text(value: object) -> str:
    """Represent one input record on one UTF-8 text line."""
    return " ".join(str(value or "").split())


def _download_split(
    dataset: str,
    split: str,
    output_dir: Path,
    page_size: int,
    timeout: int,
) -> Dict[str, object]:
    jsonl_path = output_dir / f"{split}_raw.jsonl"
    text_path = output_dir / f"{split}_text.txt"
    jsonl_tmp = output_dir / f".{split}_raw.jsonl.tmp"
    text_tmp = output_dir / f".{split}_text.txt.tmp"

    offset = 0
    expected_total = None
    features: List[Dict[str, object]] = []

    try:
        with jsonl_tmp.open("w", encoding="utf-8") as jsonl_handle, text_tmp.open(
            "w", encoding="utf-8"
        ) as text_handle:
            while expected_total is None or offset < expected_total:
                page = _request_page(
                    dataset=dataset,
                    split=split,
                    offset=offset,
                    page_size=page_size,
                    timeout=timeout,
                )
                if expected_total is None:
                    expected_total = int(page["num_rows_total"])
                    features = list(page.get("features", []))

                rows = page.get("rows", [])
                if not rows:
                    raise RuntimeError(
                        f"{split}: API returned no rows at offset {offset} "
                        f"before expected total {expected_total}"
                    )

                for wrapped_row in rows:
                    row_index = int(wrapped_row["row_idx"])
                    if row_index != offset:
                        raise RuntimeError(
                            f"{split}: expected row {offset}, received {row_index}"
                        )
                    row = dict(wrapped_row["row"])
                    jsonl_handle.write(json.dumps(row, ensure_ascii=False) + "\n")
                    text_handle.write(_normalise_text(row.get("input")) + "\n")
                    offset += 1

                print(f"{split}: downloaded {offset}/{expected_total}", flush=True)

        if offset != expected_total:
            raise RuntimeError(
                f"{split}: downloaded {offset} rows; expected {expected_total}"
            )
        os.replace(jsonl_tmp, jsonl_path)
        os.replace(text_tmp, text_path)
    except Exception:
        jsonl_tmp.unlink(missing_ok=True)
        text_tmp.unlink(missing_ok=True)
        raise

    return {
        "split": split,
        "rows": offset,
        "raw_jsonl": jsonl_path.name,
        "input_text": text_path.name,
        "features": features,
    }


def download_dataset(
    dataset: str,
    output_dir: Path,
    splits: Iterable[str],
    page_size: int,
    timeout: int,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    split_results = [
        _download_split(dataset, split, output_dir, page_size, timeout)
        for split in splits
    ]
    manifest = {
        "dataset": dataset,
        "source": f"https://huggingface.co/datasets/{dataset}",
        "downloaded_at_utc": datetime.now(timezone.utc).isoformat(),
        "format": {
            "*_raw.jsonl": "One JSON object per row with instruction, input, and output.",
            "*_text.txt": "The input policy descriptions only, one record per line.",
        },
        "splits": split_results,
    }
    manifest_path = output_dir / "manifest.json"
    manifest_tmp = output_dir / ".manifest.json.tmp"
    with manifest_tmp.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    os.replace(manifest_tmp, manifest_path)
    return manifest_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", default=DEFAULT_DATASET)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/text-to-odrl-dataset-v1/raw"),
    )
    parser.add_argument("--splits", nargs="+", default=list(DEFAULT_SPLITS))
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--timeout", type=int, default=60)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if not 1 <= args.page_size <= 100:
        raise ValueError("--page-size must be between 1 and 100")
    manifest = download_dataset(
        dataset=args.dataset,
        output_dir=args.output_dir,
        splits=args.splits,
        page_size=args.page_size,
        timeout=args.timeout,
    )
    print(f"Raw dataset written successfully. Manifest: {manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
