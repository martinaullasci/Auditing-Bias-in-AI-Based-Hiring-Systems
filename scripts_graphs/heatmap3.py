import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# LOAD CSV
df = pd.read_csv("final_bias_audit_results.csv")

# CLEAN DATA
df["Gender"] = df["Gender"].astype(str).str.strip()
df["Level"] = df["Level"].astype(str).str.strip()

# DEFINE RANKING CONTEXTS
group_cols = ["Job", "Level", "Version"]

# COMPUTE RANKS
df["Rank"] = (
    df.groupby(group_cols)["Similarity_Score"]
      .rank(method="first", ascending=False)
)

# PREPARE HEATMAP
levels = ["JR", "MID", "SR", "MGR"]
k_values = [1, 3, 5]

heatmap_data = []

# COMPUTE RD = TKR_M - TKR_F
for k in k_values:

    row = []

    for level in levels:

        subset = df[df["Level"] == level]

        included = subset["Rank"] <= k

        tkr = (
            included.groupby(subset["Gender"])
            .mean()
        )

        tkr_m = tkr["M"]
        tkr_f = tkr["F"]

        rd = tkr_m - tkr_f

        row.append(rd)

    heatmap_data.append(row)

heatmap_data = np.array(heatmap_data)

# CUSTOM COLORMAP
custom_cmap = LinearSegmentedColormap.from_list(
    "custom",
    ["#edf8e9", "#bae4b3", "#74c476", "#238b45"]
)

# PLOT
fig, ax = plt.subplots(figsize=(7, 5))

im = ax.imshow(
    heatmap_data,
    cmap=custom_cmap,
    aspect="auto"
)

# AXIS LABELS
ax.set_xticks(np.arange(len(levels)))
ax.set_xticklabels(levels, fontsize=18)

ax.set_yticks(np.arange(len(k_values)))
ax.set_yticklabels(
    ["Top-1", "Top-3", "Top-5"],
    fontsize=18
)

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
    "Risk Difference (RD)",
    fontsize=22
)

cbar.ax.tick_params(labelsize=18)

# LAYOUT
plt.tight_layout()

# SAVE
plt.savefig(
    "gender_topk_heatmap.png",
    dpi=300
)

# SHOW
plt.show()