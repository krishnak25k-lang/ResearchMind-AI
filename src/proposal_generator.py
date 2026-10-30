from src.rag import ask_researchmind


def generate_research_proposal(gap):

    """
    Generate a potential research proposal
    from a research gap using the existing RAG system.
    """

    proposal_question = f"""
You are ResearchMind AI, an academic research
proposal assistant.

The user has identified the following potential
research gap:

==================================================
POTENTIAL RESEARCH GAP
==================================================

{gap}

==================================================

Using ONLY the evidence retrieved from the
indexed research papers, develop a possible
research proposal.

IMPORTANT:

- Do not invent facts about existing papers.
- Do not claim that the proposed idea is definitely novel.
- Clearly distinguish evidence from the papers
  and your proposed research direction.
- If information is unavailable, write:
  "Not specified in the indexed papers."
- The proposal is a POSSIBLE research direction
  and requires further literature verification.

Create the proposal using the following structure:

==================================================
1. PROPOSED RESEARCH TITLE
==================================================

Give a clear academic research title.

==================================================
2. RESEARCH PROBLEM
==================================================

Explain the problem identified from the
existing research.

==================================================
3. RESEARCH GAP
==================================================

Explain what appears to be missing or insufficient
in the existing research.

==================================================
4. PROPOSED IDEA
==================================================

Explain the proposed approach to investigate
the identified gap.

==================================================
5. OBJECTIVES
==================================================

Provide 3 to 5 clear research objectives.

==================================================
6. RESEARCH QUESTIONS
==================================================

Provide important research questions that
the proposed study could investigate.

==================================================
7. PROPOSED METHODOLOGY
==================================================

Explain:

- Data collection
- Data preprocessing
- Feature engineering if required
- Model/algorithm
- Training
- Testing
- Evaluation

Do not invent a specific dataset unless the
indexed papers support it.

==================================================
8. POSSIBLE TECHNOLOGIES
==================================================

Suggest suitable technologies or tools.

Clearly mark these as:

"Proposed technology"

rather than claiming that existing papers
used them.

==================================================
9. DATASET REQUIREMENTS
==================================================

Explain what type of dataset would be required.

If the existing papers mention datasets,
describe them.

If not:

"Dataset requirement is not specified in
the indexed papers."

==================================================
10. EVALUATION METRICS
==================================================

Suggest suitable evaluation metrics.

Clearly identify them as proposed metrics.

==================================================
11. EXPECTED OUTCOME
==================================================

Explain what the proposed research could
potentially achieve.

Do not present expected outcomes as proven results.

==================================================
12. EXPECTED CONTRIBUTION
==================================================

Explain how the proposed research could
contribute to the research area.

==================================================
13. LIMITATIONS
==================================================

Identify possible limitations of the proposed
research.

==================================================
14. FUTURE EXTENSIONS
==================================================

Suggest possible future extensions.

==================================================
15. NOVELTY WARNING
==================================================

Clearly state:

"This proposal represents a potential research
direction derived from the indexed literature.
It does not establish that the idea is novel.
A comprehensive literature review is required
before claiming research novelty."

==================================================
FINAL RESEARCH PROPOSAL SUMMARY
==================================================

Provide a concise summary containing:

Title:
Research Gap:
Proposed Approach:
Main Objective:
Expected Contribution:
"""

    answer, sources = ask_researchmind(
        proposal_question
    )

    return answer, sources