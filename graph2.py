import pandas as pd
import matplotlib.pyplot as plt


# LOAD CSV

df = pd.read_csv("final_bias_audit_results.csv")


# CLEAN DATA

df["Nationality"] = df["Nationality"].astype(str).str.strip()


# CREATE NATIONALITY PAIRS

pivot_df = df.pivot_table(
    index=["Job", "Level", "Gender", "Version"],
    columns="Nationality",
    values="Similarity_Score"
).reset_index()


# COMPUTE DIFFERENCES VS ITALY

pivot_df["AL_IT"] = pivot_df["AL"] - pivot_df["IT"]
pivot_df["BR_IT"] = pivot_df["BR"] - pivot_df["IT"]
pivot_df["MO_IT"] = pivot_df["MO"] - pivot_df["IT"]


# COMPUTE MEAN DIFFERENCES

means = [
    pivot_df["AL_IT"].mean(),
    pivot_df["BR_IT"].mean(),
    pivot_df["MO_IT"].mean()
]


# LABELS AND COLORS

labels = ["AL-IT", "BR-IT", "MO-IT"]

colors = ["#a6cee3", "#1f78b4", "#33a02c"]


# CREATE BAR CHART

plt.figure(figsize=(9, 4))

bars = plt.bar(
    labels,
    means,
    color=colors
)


# AXIS LABEL

plt.ylabel(
    "Mean diff. in cos. sim.",
    fontsize=22
)


# TICKS

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)


# LEGEND

plt.legend(
    bars,
    ["Albanian", "British", "Moroccan"],
    fontsize=16
)

# LAYOUT
plt.subplots_adjust(top=0.93, bottom=0.12, left=0.25)

plt.savefig(
    "nationality_mean_difference.png",
    dpi=300
)

# SHOW FIGURE

plt.show()