import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# LOAD CSV

df = pd.read_csv("final_bias_audit_results.csv")


# CLEAN DATA

df["Nationality"] = df["Nationality"].astype(str).str.strip()


# DEFINE RANKING CONTEXTS

group_cols = ["Job", "Level", "Version"]


# COMPUTE RANKS

df["Rank"] = (
    df.groupby(group_cols)["Similarity_Score"]
      .rank(method="first", ascending=False)
)


# FUNCTION TO COMPUTE TKR

def compute_tkr(k):

    included = df["Rank"] <= k

    tkr = (
        included.groupby(df["Nationality"])
        .mean()
    )

    return tkr


# COMPUTE TOP-K RATES

k_values = [1, 3, 5]

AL_rates = []
BR_rates = []
IT_rates = []
MO_rates = []

for k in k_values:

    tkr = compute_tkr(k)

    AL_rates.append(tkr["AL"])
    BR_rates.append(tkr["BR"])
    IT_rates.append(tkr["IT"])
    MO_rates.append(tkr["MO"])


# BAR POSITIONS

x = np.arange(len(k_values))

width = 0.18


# FIGURE

fig, ax = plt.subplots(figsize=(9, 6))

# Colors
colors = {
    "AL": "#a6cee3",
    "BR": "#1f78b4",
    "IT": "#b2df8a",
    "MO": "#33a02c"
}


# BARS

ax.bar(
    x - 1.5 * width,
    AL_rates,
    width,
    label="AL",
    color=colors["AL"]
)

ax.bar(
    x - 0.5 * width,
    BR_rates,
    width,
    label="BR",
    color=colors["BR"]
)

ax.bar(
    x + 0.5 * width,
    IT_rates,
    width,
    label="IT",
    color=colors["IT"]
)

ax.bar(
    x + 1.5 * width,
    MO_rates,
    width,
    label="MO",
    color=colors["MO"]
)


# LABELS

ax.set_xlabel(
    "K",
    fontsize=22
)

ax.set_ylabel(
    "Top-K inclusion rate (TKR)",
    fontsize=22
)


# TICKS

ax.set_xticks(x)
ax.set_xticklabels(["1", "3", "5"])

ax.tick_params(axis='both', labelsize=18)


# LEGEND

ax.legend(
    title="Nationality",
    fontsize=18,
    title_fontsize=20,
    ncol=1,
    loc="upper left"
)


# Y LIMIT

ax.set_ylim(0, 1.05)


# CLEAN STYLE

#ax.spines["top"].set_visible(False)
#ax.spines["right"].set_visible(False)


# LAYOUT

plt.tight_layout()


# SAVE

plt.savefig(
    "nationality_topk_inclusion.png",
    dpi=300
)


# SHOW

plt.show()