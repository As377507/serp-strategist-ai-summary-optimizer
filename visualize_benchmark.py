"""
Visualize time and entity count comparison between original and optimized analysis
from previous benchmark JSON results.
"""

import json
import matplotlib.pyplot as plt

# Load entity analysis results
with open("examples/how-to_guide_on_website_speed_optimization.json", "r", encoding="utf-8") as f:
    original_data = json.load(f)

with open("examples/product_comparison_article.json", "r", encoding="utf-8") as f:
    optimized_data = json.load(f)
    
with open("examples/technical_explanation_of_googles_search_algorithm.json", "r", encoding="utf-8") as f:
    optimized_data = json.load(f)

# Manually set time values from previous benchmarking
original_time = 3.2  # Update with actual time for original
optimized_time = 1.5  # Update with actual time for optimized

# Extract entity counts
original_entities = len(original_data["entity_analysis"]["entities"])
optimized_entities = len(optimized_data["entity_analysis"]["entities"])

# Prepare data for visualization
labels = ["Original", "Optimized"]
entity_counts = [original_entities, optimized_entities]
times = [original_time, optimized_time]

# Plot the comparison charts
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Bar chart for entity count
ax[0].bar(labels, entity_counts, color=["steelblue", "mediumseagreen"])
ax[0].set_title("Entity Count")
ax[0].set_ylabel("Number of Entities")

# Bar chart for processing time
ax[1].bar(labels, times, color=["steelblue", "mediumseagreen"])
ax[1].set_title("Processing Time")
ax[1].set_ylabel("Seconds")

plt.suptitle("Entity Analysis: Original vs Optimized Performance", fontsize=14)
plt.tight_layout()
plt.savefig("visuals/benchmark_comparison.png")
plt.show()

print("\n✅ Benchmark comparison chart saved as visuals/benchmark_comparison.png")
