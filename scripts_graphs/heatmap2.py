import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# LOAD CSV
df = pd.read_csv("final_bias_audit_results.csv")

# CLEAN DATA
df["Nationality"] = df["Nationality"].astype(str).str.strip()
df["Level"] = df["Level"].astype(str).str.strip()

# DEFINE MATCHED PAIRS

pair_cols = [
    "Job",
    "Level",
    "Gender",
    "Version"
]

# PIVOT NATIONALITY SCORES
pivot_df = df.pivot_table(
    index=pair_cols,
    columns="Nationality",
    values="Similarity_Score"
).reset_index()

# COMPUTE DIFFERENCES VS IT
pivot_df["AL_IT"] = (
    pivot_df["AL"] - pivot_df["IT"]
)

pivot_df["BR_IT"] = (
    pivot_df["BR"] - pivot_df["IT"]
)

pivot_df["MO_IT"] = (
    pivot_df["MO"] - pivot_df["IT"]
)

# MEAN DIFFERENCES BY LEVEL
mean_diff = (
    pivot_df.groupby("Level")[["AL_IT", "BR_IT", "MO_IT"]]
    .mean()
)

# Desired order
levels = ["JR", "MID", "SR", "MGR"]

# HEATMAP DATA
heatmap_data = np.array([
    [mean_diff.loc[level, "AL_IT"] for level in levels],
    [mean_diff.loc[level, "BR_IT"] for level in levels],
    [mean_diff.loc[level, "MO_IT"] for level in levels]
])

# CUSTOM COLORMAP
custom_cmap = LinearSegmentedColormap.from_list(
    "custom",
    ["#edf8e9", "#bae4b3", "#74c476", "#238b45"]
)

# PLOT
fig, ax = plt.subplots(figsize=(9, 6))

im = ax.imshow(
    heatmap_data,
    cmap=custom_cmap,
    aspect="auto"
)

# AXES
ax.set_xticks(np.arange(len(levels)))
ax.set_xticklabels(
    levels,
    fontsize=18
)

ax.set_yticks(np.arange(3))
ax.set_yticklabels(
    ["AL-IT", "BR-IT", "MO-IT"],
    fontsize=18
)

# LABELS
ax.set_xlabel(
    "Hierarchy Level",
    fontsize=22
)

ax.set_ylabel(
    "Nationality comparison",
    fontsize=22
)

# COLORBAR
cbar = plt.colorbar(im)

cbar.set_label(
    "Mean cosine similarity difference",
    fontsize=22
)

cbar.ax.tick_params(labelsize=18)

# LAYOUT
plt.tight_layout()

# SAVE
plt.savefig(
    "nationality_score_heatmap.png",
    dpi=300
)

# SHOW
plt.show()