import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# LOAD CSV

df = pd.read_csv("final_bias_audit_results.csv")


# CLEAN DATA

df["Gender"] = df["Gender"].astype(str).str.strip()


# GLOBAL THRESHOLD ANALYSIS
# Thresholds
thresholds = [0.10, 0.20, 0.30]

female_sr = []
male_sr = []


# COMPUTE SELECTION RATES

for t in thresholds:

    # Number of selected CVs
    top_n = int(len(df) * t)

    # Rank globally by similarity score
    ranked_df = df.sort_values(
        by="Similarity_Score",
        ascending=False
    )

    # Top selected CVs
    selected = ranked_df.head(top_n)

    # Binary selection indicator
    df["Selected"] = 0
    df.loc[selected.index, "Selected"] = 1

    # Selection rate by gender
    sr = (
        df.groupby("Gender")["Selected"]
        .mean()
    )

    female_sr.append(sr["F"])
    male_sr.append(sr["M"])


# LABELS

threshold_labels = [
    "Top 10%",
    "Top 20%",
    "Top 30%"
]


# BAR POSITIONS

x = np.arange(len(threshold_labels))
width = 0.34


# FIGURE

fig, ax = plt.subplots(figsize=(8, 5))

# Colors
female_color = "#33a02c"
male_color   = "#b2df8a"

# Bars
ax.bar(
    x - width/2,
    female_sr,
    width,
    label="Female (F)",
    color=female_color
)

ax.bar(
    x + width/2,
    male_sr,
    width,
    label="Male (M)",
    color=male_color
)


# LABELS

ax.set_xlabel(
    "Target pass rate (global threshold)",
    fontsize=22
)

ax.set_ylabel(
    "Selection rate",
    fontsize=22
)

ax.set_xticks(x)
ax.set_xticklabels(
    threshold_labels,
    fontsize=18
)

ax.tick_params(axis="y", labelsize=18)


# LEGEND

ax.legend(fontsize=16)


# Y RANGE

ax.set_ylim(0, 0.35)


# CLEAN STYLE

#ax.spines["top"].set_visible(False)
#ax.spines["right"].set_visible(False)


# LAYOUT

plt.tight_layout()


# SAVE

plt.savefig(
    "gender_threshold_selection_rates.png",
    dpi=300
)


# SHOW

plt.show()