"""
Flask API that integrates all analyzers and returns a JSON summary.
"""

from flask import Flask, request, jsonify
from serp_analyzer.content_analyzer import ContentAnalyzer
from serp_analyzer.entity_analyzer import EntityAnalyzer
from serp_analyzer.ai_summary_scorer import AISummaryScorer
from optimize_large_content import analyze_entities_optimized, extract_plain_text

import markdown
from bs4 import BeautifulSoup

app = Flask(__name__)

# Initialize analyzers
content_analyzer = ContentAnalyzer()
entity_analyzer = EntityAnalyzer()
ai_summary_scorer = AISummaryScorer()

@app.route('/')
def home():
    return "✅ SERP Strategist API is running. POST content to /analyze"


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    if not data or 'content' not in data or 'type' not in data:
        return jsonify({'error': 'Missing content or type (html or markdown)'}), 400

    content = data['content']
    content_type = data['type'].lower()

    # 1. Structure analysis
    structure = content_analyzer.analyze_content_structure(content, content_type)

    # 2. Convert content to plain text for NER
    if content_type == 'markdown':
        html = markdown.markdown(content)
    else:
        html = content
    plain_text = BeautifulSoup(html, 'html.parser').get_text()

    # 3. Entity analysis
    # entity_data = entity_analyzer.analyze_entities(plain_text)
    plain_text = extract_plain_text(content, content_type)
    entity_data = analyze_entities_optimized(content, content_type)
    
    # 4. AI Summary score
    score_data = ai_summary_scorer.calculate_ai_summary_score(structure, entity_data)

    return jsonify({
        'structure_analysis': structure,
        'entity_analysis': entity_data,
        'summary_score': score_data
    })

if __name__ == '__main__':
    app.run(debug=True)
