import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# LOAD DATA

df = pd.read_csv("final_bias_audit_results.csv")


# CLEAN

df["Gender"] = df["Gender"].astype(str).str.strip()


# CREATE PAIRS

pivot_df = df.pivot_table(
    index=["Job", "Level", "Nationality", "Version"],
    columns="Gender",
    values="Similarity_Score"
).reset_index()


# DIFFERENCE

pivot_df["Difference"] = pivot_df["M"] - pivot_df["F"]


# MANUAL BIN EDGES

bin_edges = np.arange(
    -0.0011,
    0.0149,
    0.00075
)


# FIGURE

plt.figure(figsize=(8,5))

plt.hist(
    pivot_df["Difference"],
    bins=20,
    color="#33a02c"
)


# LABELS

plt.xlabel(
    "Difference in cosine similarity (M — F)",
    fontsize=22
)

plt.ylabel(
    "Count",
    fontsize=22
)


# TICKS

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)


# LAYOUT

plt.tight_layout()


# SAVE

plt.savefig(
    "gender_difference_histogram.png",
    dpi=300
)

plt.show()