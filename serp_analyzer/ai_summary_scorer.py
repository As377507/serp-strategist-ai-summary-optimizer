"""
Evaluates AI summary readiness based on structural and entity features.
"""

class AISummaryScorer:
    def calculate_ai_summary_score(self, structure: dict, entity_data: dict) -> dict:
        """
        Computes a score from 0 to 100 indicating likelihood of inclusion in AI summaries.

        Args:
            structure (dict): Output from ContentAnalyzer.
            entity_data (dict): Output from EntityAnalyzer.

        Returns:
            dict: Score, summary-worthy content, and improvement recommendations.
        """
        score = 0
        recommendations = []
        highlights = []

        # Heading presence
        if any(h['level'] == 1 for h in structure.get('headings', [])):
            score += 10
        else:
            recommendations.append("Recommendation: Add a clear H1 heading to define the main topic.")

        # Paragraph length and clarity
        para_lengths = [p['length'] for p in structure.get('paragraphs', [])]
        if para_lengths:
            avg_len = sum(para_lengths) / len(para_lengths)
            if avg_len < 150:
                score += 10
            else:
                recommendations.append("Recommendation: Break down long paragraphs into shorter, more digestible chunks.")

        # List usage
        if structure.get('lists'):
            score += 10
            highlights.extend(structure['lists'])
        else:
            recommendations.append("Recommendation: Incorporate ordered or unordered lists to present information concisely.")

        # QA patterns
        if structure.get('question_answer_patterns') and structure.get('direct_answer_statements'):
            score += 20
            highlights.extend(structure['question_answer_patterns'])
            highlights.extend(structure['direct_answer_statements'])
        else:
            recommendations.append("Recommendation: Integrate explicit question-answer patterns to signal direct information.")

        # Entities
        if entity_data['entity_density'] >= 5:
            score += 15
        else:
            recommendations.append("Recommendation: Increase entity density.")

        if entity_data['relationships']:
            score += 10

        # Content richness bonus
        if len(structure['headings']) > 3:
            score += 5
        if len(structure['paragraphs']) > 2:
            score += 10

        # Cap score
        score = min(score, 100)

        return {
            'ai_summary_score': score,
            'summary_worthy_sections': highlights,
            'recommendations': recommendations
        }
