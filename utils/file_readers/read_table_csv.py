import csv
from io import StringIO
from typing import Dict, Any

import pandas as pd
from contracts.file_readers import ReaderOutput


def _apply_header_heuristic(df: pd.DataFrame) -> pd.DataFrame:
    """
    Decide whether the first row is a header or data.

    - If the first row is all numeric (after comma→dot replace), we keep it as data
      and assign synthetic column names: "0", "1", ...
    - If there is at least one non-numeric cell, we treat the first row as header.

    Returns a DataFrame with:
        - proper column names (either from header row or "0","1",...)
        - data rows only (header row removed if used as header)
    """
    if df.empty:
        # No data at all; just name columns "0", "1", ...
        df.columns = [str(i) for i in range(df.shape[1])]
        return df

    # Look at first row
    first_row = df.iloc[0].astype(str).str.replace(",", ".")
    numeric = pd.to_numeric(first_row, errors="coerce")

    # If all values are numeric → treat as data (no header row)
    if numeric.notna().all():
        df.columns = [str(i) for i in range(df.shape[1])]
        return df

    # Otherwise: treat first row as header
    df = df.iloc[1:].reset_index(drop=True)
    df.columns = [str(v) for v in first_row]
    return df


def read_csv(path: str) -> ReaderOutput:
    """
    FileReaderFn-compatible CSV/table reader.

    Behaviour:
        - Excel (.xls/.xlsx):
            * Read with header=None.
            * Apply header heuristic:
                - First row all numeric   -> column keys: "0", "1", ...
                - Otherwise               -> first row used as header strings.
        - Text files:
            * Read full file as text.
            * Case-insensitive 'end data' splits data vs metadata:
                - Data before 'end data'
                - Metadata after, parsed as "key: value"
            * Data block parsed via pandas.read_csv with whitespace delimiter.
            * On failure, fallback to csv.reader using the same data lines.
        - Output:
            * Each column under a string key (header-or-index).
            * Metadata dict (if any) under key "meta".
    """

    # -------- Excel handling --------
    if path.lower().endswith((".xls", ".xlsx")):
        # Read EVERYTHING as data; decide header ourselves.
        df = pd.read_excel(path, header=None)
        df = _apply_header_heuristic(df)

        output: Dict[str, Any] = {}
        for col in df.columns:
            series = df[col].astype(str).str.replace(",", ".")
            numeric = pd.to_numeric(series, errors="ignore")
            output[str(col)] = numeric.tolist()

        return output

    # -------- Text file handling --------
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    lower = content.lower()
    marker = "end data"
    meta_dict: Dict[str, str] = {}

    # Split into data and metadata (case-insensitive marker)
    if marker in lower:
        idx = lower.index(marker)
        data_part = content[:idx]                    # preserve original case
        meta_part = content[idx + len(marker):]      # preserve original case

        data_lines = [ln for ln in data_part.splitlines() if ln.strip()]

        for line in meta_part.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                meta_dict[key.strip()] = value.strip()
    else:
        data_lines = [ln for ln in content.splitlines() if ln.strip()]

    # FileReaderFn(path) has no skip_lines argument, so we fix it at 0 here.
    skip_lines = 0
    effective_lines = data_lines[skip_lines:]

    # -------- Try pandas first --------
    try:
        df = pd.read_csv(
            StringIO("\n".join(effective_lines)),
            delim_whitespace=True,
            na_values=["NaN"],
            engine="python",
            header=None,        # we handle header manually
        )
    except Exception:
        # -------- Fallback: csv.reader on same lines --------
        text = "\n".join(effective_lines)

        # Try to sniff delimiter on the data block
        try:
            sample = text[:2048]
            dialect = csv.Sniffer().sniff(sample)
            delimiter = dialect.delimiter
        except csv.Error:
            delimiter = ","

        reader = csv.reader(StringIO(text), delimiter=delimiter)
        rows = [row for row in reader if row]
        df = pd.DataFrame(rows)

    # Apply header heuristic
    df = _apply_header_heuristic(df)

    # -------- Build ReaderOutput --------
    output: Dict[str, Any] = {}

    for col in df.columns:
        series = df[col].astype(str).str.replace(",", ".")
        numeric = pd.to_numeric(series, errors="ignore")
        output[str(col)] = numeric.tolist()

    if meta_dict:
        output["meta"] = meta_dict

    return output
