"""
Extracts named entities, calculates entity density, and finds basic relationships.
"""

import spacy
from collections import Counter
from itertools import combinations

class EntityAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def analyze_entities(self, text: str) -> dict:
        """
        Performs entity recognition and relationship mapping.

        Args:
            text (str): Input content as plain text.

        Returns:
            dict: Contains entities, density, and relationships.
        """
        doc = self.nlp(text)
        entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
        total_words = len([token.text for token in doc if token.is_alpha])
        entity_density = round(len(entities) / total_words * 100, 2) if total_words else 0.0

        # Count co-occurring entities in same sentence
        relationships = set()
        for sent in doc.sents:
            ents_in_sent = [ent for ent in sent.ents if ent.label_ in ('PERSON', 'ORG', 'GPE', 'PRODUCT')]
            for ent1, ent2 in combinations(ents_in_sent, 2):
                pair = f"'{ent1.text}' ({ent1.label_}) is mentioned with '{ent2.text}' ({ent2.label_})"
                relationships.add(pair)

        return {
            'entities': entities,
            'entity_density': entity_density,
            'relationships': list(relationships)
        }
