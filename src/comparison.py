from src.rag import ask_researchmind


def compare_papers(question):
    """
    Compare research papers using the existing RAG system.
    """

    comparison_question = f"""
You are ResearchMind AI, a research literature
comparison assistant.

The user wants to compare research papers.

USER REQUEST:
{question}

Analyze ONLY the evidence retrieved from the
indexed research papers.

Create a structured literature comparison.

==================================================
PAPER-BY-PAPER ANALYSIS
==================================================

For every paper that appears in the retrieved
evidence, identify:

1. Research Problem
2. Objectives
3. Methodology
4. Dataset
5. Technologies
6. Key Results
7. Limitations
8. Future Work

Clearly identify which information belongs to
which paper.

==================================================
COMPARISON MATRIX
==================================================

Create a table in Markdown.

Use this structure:

| Category | Paper 1 | Paper 2 | Paper 3 |
|----------|---------|---------|---------|
| Problem | | | |
| Objectives | | | |
| Methodology | | | |
| Dataset | | | |
| Technologies | | | |
| Results | | | |
| Limitations | | | |
| Future Work | | | |

If there are more or fewer papers, adjust the
columns accordingly.

Do NOT invent information.

If something is unavailable, write:

"Not specified"

==================================================
SIMILARITIES
==================================================

Identify the important similarities between
the research papers.

==================================================
DIFFERENCES
==================================================

Identify the important differences between
the research papers.

Focus especially on:

- methodology
- algorithms
- datasets
- technologies
- results

==================================================
COMMON LIMITATIONS
==================================================

Identify limitations shared by multiple papers.

Explain which papers have each limitation.

==================================================
FUTURE RESEARCH DIRECTIONS
==================================================

Combine the future-work suggestions from the
papers.

Identify areas that appear repeatedly.

==================================================
POTENTIAL RESEARCH OPPORTUNITIES
==================================================

Based ONLY on the evidence from the papers,
identify possible research opportunities.

For each opportunity provide:

Opportunity:
Why it may be useful:
Supporting paper(s):
Evidence:

IMPORTANT:

These are potential research opportunities,
NOT confirmed novel research gaps.

Do not claim that an idea is definitely new.

==================================================
RULES
==================================================

1. Use only information from the research papers.
2. Do not hallucinate.
3. Do not invent datasets.
4. Do not invent algorithms.
5. Do not invent accuracy values.
6. Do not invent limitations.
7. Do not invent future work.
8. If information is unavailable, write
   "Not specified".
9. Clearly distinguish between papers.
10. Base potential research opportunities on
    evidence from the papers.
"""

    answer, sources = ask_researchmind(
        comparison_question
    )

    return answer, sources