from src.rag import ask_researchmind


def detect_research_gaps(question):
    """
    Detect potential research gaps from indexed
    research papers using RAG.
    """

    gap_question = f"""
You are ResearchMind AI, an AI research gap
analysis assistant.

Your task is to analyze the indexed research
papers and identify POTENTIAL research gaps.

USER REQUEST:

{question}

==================================================
STEP 1 - EXISTING RESEARCH
==================================================

Identify what the existing research papers
have already done.

For each paper identify:

- Research problem
- Objective
- Methodology
- Dataset
- Technology
- Main results

==================================================
STEP 2 - LIMITATIONS
==================================================

Identify limitations explicitly mentioned
in the research papers.

Do not invent limitations.

For every limitation mention the paper that
reported it.

==================================================
STEP 3 - FUTURE WORK
==================================================

Identify future work suggested by the papers.

Explain which paper suggested each direction.

==================================================
STEP 4 - COMMON PROBLEMS
==================================================

Find problems or limitations that appear
in multiple research papers.

Explain why these may represent areas
requiring further investigation.

==================================================
STEP 5 - CONTRADICTIONS
==================================================

Look for differences or contradictions
between the papers.

Examples:

- Different algorithms produce different results.
- Different datasets produce different outcomes.
- One paper solves a problem that another paper
  identifies as a limitation.

==================================================
STEP 6 - POTENTIAL RESEARCH GAPS
==================================================

Identify potential research gaps.

For each gap use this format:

--------------------------------------------------

Potential Gap #1

Gap:
Explain what appears to be missing.

Evidence:
Explain which paper(s) support this observation.

Existing Approach:
Explain what existing papers currently do.

Limitation:
Explain the limitation.

Potential Research Direction:
Suggest what could be investigated.

Novelty Status:
"Requires further literature verification"

--------------------------------------------------

==================================================
STEP 7 - PRIORITY
==================================================

Rank the potential gaps:

HIGH
MEDIUM
LOW

Consider:

- Appears in multiple papers
- Important limitation
- Repeated future work
- Significant unresolved problem

==================================================
FINAL SUMMARY
==================================================

Provide:

1. Most important potential research gap
2. Supporting papers
3. Main evidence
4. Potential research direction
5. Why further research may be useful

IMPORTANT RULES:

1. Use ONLY evidence from retrieved research papers.
2. Do not invent facts.
3. Do not invent datasets.
4. Do not invent results.
5. Do not invent limitations.
6. Do not claim an idea is definitely novel.
7. Use "potential research gap".
8. Clearly identify supporting papers.
9. If evidence is insufficient, say:
   "Insufficient evidence from the indexed papers."
10. A research gap must be verified against additional
    literature before being considered genuinely novel.
"""

    answer, sources = ask_researchmind(
        gap_question
    )

    return answer, sources