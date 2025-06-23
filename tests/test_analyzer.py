"""
tests/test_analyzer.py
Unit tests for ContentAnalyzer, EntityAnalyzer, AISummaryScorer
"""

import unittest
from serp_analyzer.content_analyzer import ContentAnalyzer
from serp_analyzer.entity_analyzer import EntityAnalyzer
from serp_analyzer.ai_summary_scorer import AISummaryScorer

class TestAnalyzers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content_analyzer = ContentAnalyzer()
        cls.entity_analyzer = EntityAnalyzer()
        cls.summary_scorer = AISummaryScorer()

    def test_html_structure(self):
        html = """
        <h1>Main Topic</h1>
        <p>What is Python? Python is a programming language.</p>
        <ul><li>Easy</li><li>Powerful</li></ul>
        """
        result = self.content_analyzer.analyze_content_structure(html, 'html')
        self.assertGreaterEqual(len(result['headings']), 1)
        self.assertIn('What is Python?', result['question_answer_patterns'])
        self.assertIn('Python is a programming language.', result['direct_answer_statements'])

    def test_markdown_structure(self):
        md = """# Heading

What is NLP? NLP is language AI.

- Tokenization
- Named Entity Recognition
"""
        result = self.content_analyzer.analyze_content_structure(md, 'markdown')
        self.assertGreaterEqual(len(result['headings']), 1, "Expected at least one heading from markdown")
        self.assertGreaterEqual(len(result['lists']), 2, "Expected list items to be detected")

    def test_entity_analysis(self):
        text = """Google was founded by Larry Page and Sergey Brin in California."""
        result = self.entity_analyzer.analyze_entities(text)
        self.assertGreaterEqual(len(result['entities']), 3)
        self.assertGreater(result['entity_density'], 0)
        self.assertTrue(any('Larry Page' in r for r in result['relationships']))

    def test_summary_score(self):
        structure = {
            'headings': [{'text': 'Intro', 'level': 1}],
            'paragraphs': [{'text': 'What is AI?', 'length': 3}, {'text': 'AI is intelligence.', 'length': 3}],
            'lists': ['Item A'],
            'question_answer_patterns': ['What is AI?'],
            'direct_answer_statements': ['AI is intelligence.']
        }
        entities = {
            'entities': [{'text': 'AI', 'label': 'TECH'}],
            'entity_density': 12.5,
            'relationships': []
        }
        score = self.summary_scorer.calculate_ai_summary_score(structure, entities)
        self.assertGreaterEqual(score['ai_summary_score'], 60)

if __name__ == '__main__':
    unittest.main()