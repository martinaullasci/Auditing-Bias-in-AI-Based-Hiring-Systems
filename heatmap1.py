import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


# LOAD CSV

df = pd.read_csv("final_bias_audit_results.csv")


# CLEAN DATA

df["Gender"] = df["Gender"].astype(str).str.strip()
df["Level"] = df["Level"].astype(str).str.strip()


# DEFINE MATCHED PAIRS

pair_cols = [
    "Job",
    "Level",
    "Nationality",
    "Version"
]


# PIVOT MALE/FEMALE SCORES

pivot_df = df.pivot_table(
    index=pair_cols,
    columns="Gender",
    values="Similarity_Score"
).reset_index()


# COMPUTE SCORE DIFFERENCE

# Difference = Male - Female


pivot_df["Diff_MF"] = (
    pivot_df["M"] - pivot_df["F"]
)


# MEAN DIFFERENCE BY LEVEL

mean_diff = (
    pivot_df.groupby("Level")["Diff_MF"]
    .mean()
)

# Desired order
levels = ["JR", "MID", "SR", "MGR"]

# Heatmap structure
heatmap_data = np.array([
    [mean_diff[level] for level in levels]
])


# CUSTOM COLORMAP

custom_cmap = LinearSegmentedColormap.from_list(
    "custom",
    ["#edf8e9", "#bae4b3", "#74c476", "#238b45"]
)


# PLOT

fig, ax = plt.subplots(figsize=(9, 4))

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

ax.set_yticks([0])
ax.set_yticklabels(
    ["M - F"],
    fontsize=18
)


# LABELS

ax.set_xlabel(
    "Hierarchy Level",
    fontsize=22
)

ax.set_ylabel(
    "Gender difference",
    fontsize=22
)


# COLORBAR

cbar = plt.colorbar(im)
cbar.ax.tick_params(labelsize=18)

cbar.set_label(
    "Mean cos. sim. diff.",
    fontsize=22
)


# LAYOUT

plt.tight_layout()


# SAVE

plt.savefig(
    "gender_score_heatmap.png",
    dpi=300
)


# SHOW

plt.show()