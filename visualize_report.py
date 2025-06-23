import json
import os
import matplotlib.pyplot as plt
from collections import Counter

# Fix overlapping and cutoff labels using layout adjustments

def visualize_headings(headings, title):
    levels = [h['level'] for h in headings]
    labels = [h['text'] for h in headings]

    plt.figure(figsize=(14, 6))
    bars = plt.bar(range(len(labels)), levels, tick_label=labels, color='skyblue')
    plt.ylabel("Heading Level", fontsize=12)
    plt.title(f"Heading Hierarchy - {title}", fontsize=14)
    plt.xticks(rotation=60, ha='right', fontsize=9)
    plt.tight_layout()
    plt.savefig(f"visuals/{title}_headings_cleaned.png")
    plt.close()

def visualize_entity_types(entities, title):
    labels = [e['label'] for e in entities]
    count = Counter(labels)

    plt.figure(figsize=(10, 5))
    bars = plt.bar(count.keys(), count.values(), color='coral')
    plt.title(f"Entity Types - {title}", fontsize=14)
    plt.ylabel("Frequency", fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.tight_layout()
    plt.savefig(f"visuals/{title}_entities_cleaned.png")
    plt.close()
    
    
def visualize_paragraph_lengths(paragraphs, title):
    lengths = [p['length'] for p in paragraphs]  # Extract paragraph lengths

    plt.figure(figsize=(10, 5))
    plt.hist(lengths, bins='auto', color='lightgreen', edgecolor='black', rwidth=0.85)
    plt.xlabel("Paragraph Length (words)", fontsize=12)
    plt.ylabel("Number of Paragraphs", fontsize=12)
    plt.title(f"Paragraph Length Distribution - {title}", fontsize=14)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.savefig(f"visuals/{title}_paragraphs_cleaned.png")  # Save improved chart
    plt.close()


# Load and visualize all three example files with cleaned formatting
example_files = {
    "how-to_guide_on_website_speed_optimization": "examples/how-to_guide_on_website_speed_optimization.json",
    "product_comparison_article": "examples/product_comparison_article.json",
    "technical_explanation_of_googles_search_algorithm": "examples/technical_explanation_of_googles_search_algorithm.json"
}

# Create visuals directory if not present
os.makedirs("visuals", exist_ok=True)

# Loop through each file and generate cleaned visuals
for title, filepath in example_files.items():
    with open(filepath, "r", encoding="utf-8") as f:
        example_data = json.load(f)

    visualize_headings(example_data["structure_analysis"]["headings"], title)
    visualize_entity_types(example_data["entity_analysis"]["entities"], title)
    visualize_paragraph_lengths(example_data["structure_analysis"]["paragraphs"], title)

"✅ Cleaned charts regenerated with improved axis labels."
