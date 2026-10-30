from src.rag import ask_researchmind


def recommend_papers(topic):
    """
    Recommend the most relevant indexed research papers
    for a given research topic.
    """

    recommendation_question = f"""
You are ResearchMind AI, an academic research
paper recommendation assistant.

The researcher is interested in:

==================================================
RESEARCH TOPIC
==================================================

{topic}

==================================================

Analyze the indexed research papers and identify
the papers that are most relevant to this topic.

Use ONLY evidence retrieved from the indexed
research papers.

Do NOT invent information.

For each relevant paper provide:

1. Paper Name
2. Relevance
3. Why the Paper is Relevant
4. Important Contribution
5. Methodology Used
6. Dataset Used
7. Technologies / Algorithms
8. Limitations
9. Connection to the Research Topic

Then provide:

==================================================
TOP RECOMMENDATION
==================================================

Identify the single most relevant paper and
explain why it is the best starting point.

==================================================
RECOMMENDED READING ORDER
==================================================

Rank the relevant papers from most relevant
to least relevant.

For each ranking explain the reason.

==================================================
RESEARCH DIRECTION
==================================================

Explain how these papers collectively help
a researcher understand the research topic.

IMPORTANT:

- Do not claim a paper is relevant without evidence.
- If information is unavailable, say:
  "Not specified in the indexed papers."
- Do not invent datasets, technologies,
  results or methodologies.
"""

    answer, sources = ask_researchmind(
        recommendation_question
    )

    return answer, sources