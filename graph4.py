import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# LOAD CSV
df = pd.read_csv("final_bias_audit_results.csv")

# CLEAN
df["Nationality"] = df["Nationality"].astype(str).str.strip()

# GLOBAL THRESHOLDS
threshold_levels = [0.10, 0.20, 0.30]

# STORE RESULTS
selection_rates = {
    "AL": [],
    "BR": [],
    "IT": [],
    "MO": []
}

# COMPUTE GLOBAL THRESHOLD SELECTION RATES
for p in threshold_levels:

    # Global cutoff corresponding to top p%
    cutoff = df["Similarity_Score"].quantile(1 - p)

    # Selected candidates
    selected = df["Similarity_Score"] >= cutoff

    # Compute selection rate for each nationality
    sr = (
        selected.groupby(df["Nationality"])
        .mean()
    )

    # Store results
    selection_rates["AL"].append(sr.get("AL", 0))
    selection_rates["BR"].append(sr.get("BR", 0))
    selection_rates["IT"].append(sr.get("IT", 0))
    selection_rates["MO"].append(sr.get("MO", 0))

# PLOT
thresholds = ["10%", "20%", "30%"]

x = np.arange(len(thresholds))
width = 0.18

fig, ax = plt.subplots(figsize=(10, 6))

colors = {
    "AL": "#a6cee3",
    "BR": "#1f78b4",
    "IT": "#b2df8a",
    "MO": "#33a02c"
}

ax.bar(
    x - 1.5 * width,
    selection_rates["AL"],
    width,
    label="AL",
    color=colors["AL"]
)

ax.bar(
    x - 0.5 * width,
    selection_rates["BR"],
    width,
    label="BR",
    color=colors["BR"]
)

ax.bar(
    x + 0.5 * width,
    selection_rates["IT"],
    width,
    label="IT",
    color=colors["IT"]
)

ax.bar(
    x + 1.5 * width,
    selection_rates["MO"],
    width,
    label="MO",
    color=colors["MO"]
)

# LABELS
ax.set_xlabel(
    "Operating point (global threshold)",
    fontsize=22
)

ax.set_ylabel(
    "Selection rate",
    fontsize=22
)

# TICKS
# TICKS
ax.set_xticks(x)
ax.set_xticklabels(
    thresholds,
    fontsize=18
)
ax.tick_params(axis="y", labelsize=18)

# LEGEND
ax.legend(
    title="Nationality",
    fontsize=18,
    title_fontsize=20
)

# Y RANGE
ax.set_ylim(0, 0.36)

# BOX AROUND GRAPH
for spine in ax.spines.values():
    spine.set_visible(True)

plt.tight_layout()

# SAVE
plt.savefig(
    "nationality_threshold_selection_rates.png",
    dpi=300
)

plt.show()