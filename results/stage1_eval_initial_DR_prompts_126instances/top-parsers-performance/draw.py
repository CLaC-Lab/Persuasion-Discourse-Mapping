import matplotlib.pyplot as plt
import numpy as np

# Data from the JSON
data = {
    "5": {"agreement_level": 5, "trial1_f1": 0.456, "trial1_size": 98, "trial2_f1": 0.449, "trial2_size": 96, "average_f1": 0.452},
    "6": {"agreement_level": 6, "trial1_f1": 0.517, "trial1_size": 74, "trial2_f1": 0.465, "trial2_size": 74, "average_f1": 0.491},
    "7": {"agreement_level": 7, "trial1_f1": 0.556, "trial1_size": 61, "trial2_f1": 0.54, "trial2_size": 58, "average_f1": 0.548},
    "8": {"agreement_level": 8, "trial1_f1": 0.668, "trial1_size": 47, "trial2_f1": 0.669, "trial2_size": 49, "average_f1": 0.669},
    "9": {"agreement_level": 9, "trial1_f1": 0.735, "trial1_size": 34, "trial2_f1": 0.746, "trial2_size": 38, "average_f1": 0.74},
}

# Extracting values
agreement_levels = [d["agreement_level"] for d in data.values()]
average_f1 = [d["average_f1"] for d in data.values()]
trial1_f1 = [d["trial1_f1"] for d in data.values()]
trial2_f1 = [d["trial2_f1"] for d in data.values()]
trial1_size = [d["trial1_size"] for d in data.values()]
trial2_size = [d["trial2_size"] for d in data.values()]

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Data
x_labels = ["5", "6", "7", "8", "9"]
average_f1 = [0.452, 0.491, 0.548, 0.669, 0.74]

# Create figure with exact 8x5 dimensions
plt.figure(figsize=(8, 5))

# Create bars with professional blue color like in the paper
bars = plt.bar(x_labels, average_f1, color='#4472C4', width=0.6)

# Add gridlines (similar to paper style)
plt.grid(axis='y', linestyle='-', alpha=0.7, zorder=0)

# Axis labels with proper academic formatting
plt.xlabel("Number of Agreeing Classifiers (n)", fontsize=17, labelpad=10)
plt.ylabel("Average F1 Score", fontsize=17, labelpad=10)

# Set y-axis limits and format to show 2 decimal places
plt.ylim(0, 1)
plt.gca().yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}',
             ha='center', va='bottom', fontsize=17)

# Clean up margins and save at high resolution
plt.tight_layout()
plt.savefig("pooling_agreement_f1.png", dpi=300, bbox_inches='tight')
# plt.show()

# # Bar Chart with Two Axes for Trial F1 Scores and Sizes
# fig, ax1 = plt.subplots(figsize=(10, 5))
# ax2 = ax1.twinx()

# bar_width = 0.2
# x = np.arange(len(agreement_levels))

# bars1 = ax1.bar(x - 0.2, trial1_f1, width=bar_width, label="Trial 1 F1", color='blue')
# bars2 = ax1.bar(x + 0.2, trial2_f1, width=bar_width, label="Trial 2 F1", color='green')
# bars3 = ax2.bar(x - 0.2, trial1_size, width=bar_width, label="Trial 1 Size", color='lightblue', alpha=0.5)
# bars4 = ax2.bar(x + 0.2, trial2_size, width=bar_width, label="Trial 2 Size", color='lightgreen', alpha=0.5)

# ax1.set_xlabel("Agreement Level")
# ax1.set_ylabel("F1 Score")
# ax2.set_ylabel("Trial Size")
# ax1.set_xticks(x)
# ax1.set_xticklabels(x_labels, rotation=30, ha="right")
# ax1.legend(loc="upper left")
# ax2.legend(loc="upper right")
# plt.title("Trial F1 Scores and Sizes per Agreement Level")
# plt.grid(axis='y')

# # Add values on top of the bars
# for bars in [bars1, bars2, bars3, bars4]:
#     for bar in bars:
#         height = bar.get_height()
#         ax1.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}', ha='center', va='bottom', fontsize=10, color='black')

# plt.show()
