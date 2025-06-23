"""
Performance optimization module for analyzing large content pieces in SERP Strategist.
Includes chunking, lightweight spaCy pipeline, and reusable text extraction.
"""

import spacy
from bs4 import BeautifulSoup
import markdown
from functools import lru_cache

# Load lightweight spaCy pipeline (NER only)
nlp = spacy.load("en_core_web_sm", disable=["parser", "textcat"])

# --- Utility: Chunk text into smaller batches for spaCy ---
def split_into_chunks(text, max_words=400):
    words = text.split()
    for i in range(0, len(words), max_words):
        yield ' '.join(words[i:i + max_words])

# --- Utility: Convert HTML or Markdown to plain text ---
def extract_plain_text(content: str, content_type: str) -> str:
    if content_type.lower() == 'markdown':
        html = markdown.markdown(content)
    else:
        html = content
    return BeautifulSoup(html, 'html.parser').get_text()

# --- Optimized Entity Analyzer for Large Content ---
def analyze_entities_optimized(content: str, content_type: str) -> list:
    plain_text = extract_plain_text(content, content_type)
    entities = []
    for chunk in split_into_chunks(plain_text):
        doc = nlp(chunk)
        entities.extend([{
            "text": ent.text,
            "label": ent.label_
        } for ent in doc.ents])
    return entities

# --- Optional: Cache entity results based on content hash (if needed) ---
@lru_cache(maxsize=64)
def analyze_entities_cached(content_hash: str, content: str, content_type: str) -> list:
    return analyze_entities_optimized(content, content_type)

# Example usage:
if __name__ == "__main__":
    with open("sample_content/Sample_Content_for_Python_Intern_Assignment.md", "r", encoding="utf-8") as f:
        sample = f.read()

    result = analyze_entities_optimized(sample, "markdown")
    print(f"✅ Optimized Entity Count: {len(result)}")
