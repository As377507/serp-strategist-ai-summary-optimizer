import requests
import json
import os
import re

# Step 1: Make sure output folder exists
os.makedirs("examples", exist_ok=True)

# Step 2: Load the markdown file
with open("Sample_Content_for_Python_Intern_Assignment.md", "r", encoding="utf-8") as f:
    content = f.read()

# Step 3: Extract each HTML block
pattern = r"## Sample \d+: (.*?)\n\n```html\n(.*?)```"
matches = re.findall(pattern, content, re.DOTALL)

# Step 4: Loop through each sample and send to API
for title, html_block in matches:
    slug = (
        title.lower()
        .replace("'", "")
        .replace(",", "")
        .replace(".", "")
        .replace("&", "and")
        .replace("  ", " ")
        .replace(" ", "_")
    )

    print(f"🔍 Analyzing: {title} → {slug}.json")

    payload = {
        "content": html_block.strip(),
        "type": "html"
    }

    try:
        res = requests.post("http://127.0.0.1:5000/analyze", json=payload)
        res.raise_for_status()
        with open(f"examples/{slug}.json", "w", encoding="utf-8") as f:
            json.dump(res.json(), f, indent=2)
        print(f"✅ Saved: examples/{slug}.json")
    except Exception as e:
        print(f"❌ Error analyzing {title}: {e}")
