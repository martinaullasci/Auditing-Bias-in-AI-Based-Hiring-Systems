import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# LOAD CSV
df = pd.read_csv("final_bias_audit_results.csv")

# CLEAN DATA
df["Nationality"] = df["Nationality"].astype(str).str.strip()
df["Level"] = df["Level"].astype(str).str.strip()

# DEFINE RANKING CONTEXT

group_cols = ["Job", "Level", "Version"]

# COMPUTE RANKS
df["Rank"] = (
    df.groupby(group_cols)["Similarity_Score"]
      .rank(method="first", ascending=False)
)

# HEATMAP CONFIG
levels = ["JR", "MID", "SR", "MGR"]
k_values = [1, 3, 5]

heatmap_data = []

# COMPUTE MAX RD VS IT
for level in levels:

    row = []

    level_subset = df[df["Level"] == level]

    for k in k_values:

        # Included profiles
        included = level_subset["Rank"] <= k

        # Top-K inclusion rate
        tkr = (
            included.groupby(level_subset["Nationality"])
            .mean()
        )

        # Risk difference vs IT baseline
        rd_al = tkr["AL"] - tkr["IT"]
        rd_br = tkr["BR"] - tkr["IT"]
        rd_mo = tkr["MO"] - tkr["IT"]

        # Maximum risk difference
        max_rd = max(rd_al, rd_br, rd_mo)

        row.append(max_rd)

    heatmap_data.append(row)

# TRANSPOSE MATRIX
heatmap_data = np.array(heatmap_data).T

# CUSTOM COLORMAP
custom_cmap = LinearSegmentedColormap.from_list(
    "custom",
    ["#edf8e9", "#bae4b3", "#74c476", "#238b45"]
)

# FIGURE
fig, ax = plt.subplots(figsize=(7, 5))

# HEATMAP
im = ax.imshow(
    heatmap_data,
    cmap=custom_cmap,
    aspect="auto"
)

# X AXIS
ax.set_xticks(np.arange(len(levels)))

ax.set_xticklabels(
    levels,
    fontsize=18
)

# Y AXIS
ax.set_yticks(np.arange(len(k_values)))

ax.set_yticklabels(
    ["Top-1", "Top-3", "Top-5"],
    fontsize=18
)

# LABELS
ax.set_xlabel(
    "Hierarchy level",
    fontsize=22
)

ax.set_ylabel(
    "Top-K",
    fontsize=22
)

# COLORBAR
cbar = plt.colorbar(im)

cbar.set_label(
    "Max RD vs IT",
    fontsize=22
)

cbar.ax.tick_params(labelsize=18)

# LAYOUT
plt.tight_layout()

# SAVE
plt.savefig(
    "nationality_topk_heatmap.png",
    dpi=300
)

# SHOW
plt.show()