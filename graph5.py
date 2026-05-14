import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# LOAD CSV

df = pd.read_csv("final_bias_audit_results.csv")


# CLEAN DATA

df["Gender"] = df["Gender"].astype(str).str.strip()


# DEFINE RANKING CONTEXTS
group_cols = ["Job", "Level", "Version"]


# COMPUTE RANKS WITHIN CONTEXT

df["Rank"] = (
    df.groupby(group_cols)["Similarity_Score"]
      .rank(method="first", ascending=False)
)


# FUNCTION TO COMPUTE TKR

def compute_tkr(k):

    # Candidate appears in Top-K?
    included = df["Rank"] <= k

    # Inclusion rate by gender
    tkr = (
        included.groupby(df["Gender"])
        .mean()
    )

    return tkr


# COMPUTE TOP-K RATES

k_values = [1, 3, 5]

female_rates = []
male_rates = []

for k in k_values:

    tkr = compute_tkr(k)

    female_rates.append(tkr["F"])
    male_rates.append(tkr["M"])


# BAR POSITIONS

x = np.arange(len(k_values))

width = 0.34


# FIGURE

fig, ax = plt.subplots(figsize=(8,5))

# Colors
female_color = "#33a02c"
male_color   ="#b2df8a"

# BARS

ax.bar(
    x - width/2,
    female_rates,
    width,
    label="Female (F)",
    color=female_color
)

ax.bar(
    x + width/2,
    male_rates,
    width,
    label="Male (M)",
    color=male_color
)


# LABELS

ax.set_xlabel(
    "K",
    fontsize=22
)

ax.set_ylabel(
    "Inclusion rate",
    fontsize=22
)


# TICKS

ax.set_xticks(x)
ax.set_xticklabels(["1", "3", "5"])

ax.tick_params(axis='both', labelsize=18)


# LEGEND

ax.legend(fontsize=18)


# Y LIMITS

ax.set_ylim(0, 0.8)


# LAYOUT

plt.tight_layout()


# SAVE

plt.savefig(
    "gender_topk_inclusion.png",
    dpi=300
)


# SHOW

plt.show()