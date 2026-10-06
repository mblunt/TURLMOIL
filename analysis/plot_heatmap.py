#!/usr/bin/env python3
"""Render scheme_matrix.csv as a binary heatmap PNG."""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

CSV = Path(__file__).parent / "scheme_matrix.csv"
OUT = Path(__file__).parent / "scheme_heatmap.png"

df = pd.read_csv(CSV)
matrix = df.pivot(index="library_a", columns="library_b", values="has_differential")

# Fill NaN explicitly before any reindexing — missing pairs are NOT differentials
matrix = matrix.fillna(0).astype(int)

# Build a unified index from the UNION of both axes to handle asymmetric CSVs
all_libs = sorted(set(matrix.index) | set(matrix.columns))
matrix = matrix.reindex(index=all_libs, columns=all_libs, fill_value=0)

# Validate completeness before sorting
assert matrix.isnull().sum().sum() == 0, "NaNs remain after fill"
assert set(matrix.index) == set(matrix.columns), "Index/column mismatch"
assert (matrix.values == matrix.values.T).all(), "Matrix is not symmetric — check CSV"

# Sort so libraries with the most differentials cluster together
order = matrix.sum(axis=1).sort_values(ascending=False).index
matrix = matrix.loc[order, order]

n = len(matrix)
fig, ax = plt.subplots(figsize=(max(12, n * 0.18), max(10, n * 0.18)))

# -1 = exclude (grey), 0 = no differential (blue), 1 = differential (red)
cmap = mcolors.ListedColormap(["#888888", "#6fbbe1", "#c0392b"])
ax.imshow(matrix.values + 1, cmap=cmap, vmin=0, vmax=2, aspect="auto", interpolation="none")

ax.set_xticks(range(n))
ax.set_yticks(range(n))
ax.set_xticklabels(matrix.columns, rotation=90, fontsize=5)
ax.set_yticklabels(matrix.index, fontsize=5)

ax.set_title("Scheme differential matrix (red = differential | grey = EXCLUDE | blue = none)", fontsize=10)
plt.tight_layout()
plt.savefig(OUT, dpi=150)
print(f"Saved: {OUT}")