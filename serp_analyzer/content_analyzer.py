"""
Analyzes the structure of HTML or Markdown content for SEO and AI summary readiness.
"""

import re
from bs4 import BeautifulSoup
import markdown

class ContentAnalyzer:
    def analyze_content_structure(self, content: str, content_type: str = 'html') -> dict:
        """
        Analyzes content structure and extracts headings, paragraphs, lists, and QA patterns.
        
        Args:
            content (str): The HTML or Markdown content.
            content_type (str): 'html' or 'markdown'

        Returns:
            dict: Dictionary containing extracted structural information.
        """
        if content_type == 'markdown':
            content = markdown.markdown(content)
        
        soup = BeautifulSoup(content, 'html.parser')
        
        headings = []
        for level in range(1, 7):
            for tag in soup.find_all(f'h{level}'):
                headings.append({'text': tag.get_text(strip=True), 'level': level})

        paragraphs = []
        for p in soup.find_all('p'):
            text = p.get_text(strip=True)
            if text:
                paragraphs.append({'text': text, 'length': len(text.split())})

        lists = []
        for tag in soup.find_all(['ul', 'ol']):
            for li in tag.find_all('li'):
                lists.append(li.get_text(strip=True))

        question_answer_patterns = []
        direct_answer_statements = []
        for para in paragraphs:
            sentences = re.split(r'(?<=[?.])\s+', para['text'])
            for i, sentence in enumerate(sentences):
                if re.match(r'(?i)\b(what|why|how|who|when|where|is|are|can|does|do|should)\b.*\?', sentence):
                    question_answer_patterns.append(sentence)
                    if i + 1 < len(sentences):
                        direct_answer_statements.append(sentences[i + 1])

        return {
            'headings': headings,
            'paragraphs': paragraphs,
            'lists': lists,
            'question_answer_patterns': question_answer_patterns,
            'direct_answer_statements': direct_answer_statements
        }
