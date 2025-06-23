# SERP Strategist - AI Content Analyzer

This project analyzes HTML or Markdown content to evaluate its readiness for inclusion in Google's AI-generated summaries using content structure, entity density, and NLP heuristics.

---

## 🌟 Why This Project Matters

With the rise of AI-powered search engines (like Google SGE and Bing Copilot), content must be easily understandable by language models to appear in summarized answers. This project helps businesses ensure their content is structured and entity-rich enough to be featured.

---

## 📦 Features

- 📊 Extracts headings, paragraphs, lists, and question-answer patterns from HTML/Markdown
- 🧠 Performs named entity recognition using spaCy
- ⚙️ Calculates AI-summary readiness score (0–100)
- 📌 Provides actionable improvement recommendations
- 🌐 Flask API endpoint for integration and automation
- 🚀 Optimized processing for large content using chunking and lightweight NLP
- 📈 Visual performance benchmark between original and optimized analyzers

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/As377507/serp-strategist-ai-summary-optimizer.git
cd serp-strategist-ai-summary-optimizer
```

### 2. Create Virtual Environment (Optional)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download spaCy Language Model
```bash
python -m spacy download en_core_web_sm
```

---

## 🧪 Run Unit Tests
```bash
python -m unittest discover -s tests
```

---

## 🌐 API Usage

### Start the Flask Server
```bash
python api_server.py
```

### Base URL
```
http://127.0.0.1:5000
```

### Available Endpoint
```
POST /analyze
```

### API Testing
```bash
python test_api.py
```

### Sample Request
```json
{
  "content": "<h1>Example</h1><p>What is AI? AI is the simulation of human intelligence.</p>",
  "type": "html"
}
```

### Sample Response
```json
{
  "structure_analysis": { ... },
  "entity_analysis": { ... },
  "summary_score": {
    "ai_summary_score": 75,
    "summary_worthy_sections": [...],
    "recommendations": [...]
  }
}
```

---

## 📂 Folder Structure
```
serp-strategist-ai-summary-optimizer/
├── serp_analyzer/
│   ├── content_analyzer.py
│   ├── entity_analyzer.py
│   └── ai_summary_scorer.py
├── api_server.py
├── test_api.py
├── optimize_large_content.py
├── visualize_benchmark.py
├── benchmark_comparison.png
├── requirements.txt
├── README.md
├── sample_content/
│   └── Sample_Content_for_Python_Intern_Assignment.md
├── examples/
│   ├── how_to_guide_on_website_speed_optimization.json
│   ├── product_comparison_article.json
│   └── technical_explanation_of_googles_search_algorithm.json
├── visuals/
│   ├── *_headings_cleaned.png //Generalize way i explain how images are stored
│   ├── *_paragraphs_cleaned.png
│   ├── *_entities_cleaned.png
│   └── benchmark_comparison.png
└── tests/
    └── test_analyzer.py
```

---

## ✅ Example Outputs

You can find example outputs (in JSON format) for real content in the `examples/` folder, generated using `test_api.py`:

- `how_to_guide_on_website_speed_optimization.json`
- `product_comparison_article.json`
- `technical_explanation_of_googles_search_algorithm.json`

---

## 📊 Visual Reports

For each of the above examples, you can generate and view:

- **Heading Hierarchies** (bar charts)
- **Paragraph Length Distribution** (histograms)
- **Entity Type Breakdown** (bar charts)
- **Entity Analysis Benchmark** (entity count vs processing time)

These are automatically saved into the `visuals/` folder using:

```bash
python visualize_report.py
python visualize_benchmark.py
```

---

## ✨ Technical Highlights

- Uses `spaCy` for NER and relationship detection
- Converts Markdown to HTML before parsing
- Extracts Q&A patterns using regular expressions
- Modular codebase designed for easy extension
- Performance optimization with:
  - `optimize_large_content.py` (NER chunking)
  - `@lru_cache` for repeated content
  - Visual time/entity comparison

---

## 💡 Explanation of My Approach

This project is modularly divided into:
- **ContentAnalyzer**: Extracts structure like headings, paragraphs, lists, Q&A patterns.
- **EntityAnalyzer**: Uses spaCy NER to identify entities and their relationships.
- **AISummaryScorer**: Computes a score using heuristics based on known AI-summary best practices.
- **API Layer**: Flask app provides a REST endpoint for integrating with any content system.
- **Visualization**: Matplotlib is used to generate visuals from example output data.
- **Optimization**: For large documents, spaCy chunking is used along with `@lru_cache` to avoid recomputation.

---

## ⚠️ Limitations and Future Improvements

### Limitations
- spaCy model (`en_core_web_sm`) is lightweight and may miss some domain-specific entities
- Entity relationships are inferred co-occurrence only (not syntactic or graph-based)
- No frontend GUI — API only
- Caching is per-session and not persisted across restarts

### Future Improvements
- Use spaCy transformer model or integrate with Google Cloud NLP for improved accuracy
- Redis/memory caching for long-term reuse
- Build a small frontend to visualize scores and suggestions interactively
- Add summary-worthy sentence detection with confidence scoring
- Deploy as a Docker container with Swagger UI for API testing

---

## 🛠️ Challenges Faced During Development

- ❗ Getting `serp_analyzer` imports to work in different environments (Colab, Windows)
- ⌛ Processing large HTML content caused spaCy to slow down → solved with chunking 
- 📦 Entity co-occurrence was hard to tune meaningfully without dependency parsing
- 🔍 Markdown handling needed consistent pre-conversion to HTML before parsing
- 🧪 API testing Issues we faced during Development
- 🧪 Some unit tests initially failed due to minor Markdown parsing quirks (e.g. missing heading hashes)
- 📤 GitHub push conflict (remote README mismatch) → resolved with force push or pull merge

---

## 👨‍💻 Author

**Akash Sen**  
Internship Assignment: SERP Strategist – AI Summary Optimization Engine

---

## 🔗 License
MIT License
