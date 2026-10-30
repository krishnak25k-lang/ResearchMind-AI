from src.rag import ask_researchmind


def generate_research_ideas(topic):
    """
    Generate new research ideas based only on
    evidence retrieved from indexed research papers.
    """

    prompt = f"""
You are ResearchMind AI, an academic research idea
generation assistant.

Analyze the indexed research papers and identify
potential new research opportunities related to:

TOPIC:
{topic}

IMPORTANT RULES:

1. Use ONLY information supported by the indexed
   research papers.
2. Do not invent research gaps.
3. Do not invent datasets, technologies, results,
   or limitations.
4. If something is not available in the papers,
   write "Not specified in the indexed papers."
5. Clearly distinguish existing research from
   proposed research.
6. Base proposed ideas on limitations, gaps,
   future work, methodologies, or technologies
   found in the papers.

For the research topic, provide:

1. Research Area
2. Existing Research
3. Identified Research Gap
4. Proposed Research Idea
5. Proposed Title
6. Problem Statement
7. Proposed Methodology
8. Technologies / Algorithms
9. Possible Dataset
10. Expected Contribution
11. Future Scope

At the end provide:

RESEARCH IDEA SUMMARY

Explain why the proposed idea could be worth
investigating based on the indexed papers.

Do not claim that the proposed idea is proven.
It is only a potential research direction.
"""

    answer, sources = ask_researchmind(prompt)

    return answer, sources