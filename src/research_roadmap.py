from src.rag import ask_researchmind


def generate_research_roadmap(research_topic):
    """
    Generate a structured research roadmap
    using the indexed research papers.
    """

    roadmap_question = f"""
You are ResearchMind AI, an academic research
planning assistant.

The researcher wants to investigate:

==================================================
RESEARCH TOPIC
==================================================

{research_topic}

==================================================

Analyze the indexed research papers and create
a practical research roadmap.

Use ONLY information supported by the retrieved
research papers when describing existing research.

Do not invent facts about the papers.

For proposed steps, clearly identify them as
RECOMMENDED RESEARCH STEPS.

Create the roadmap using the following structure:

==================================================
1. RESEARCH AREA
==================================================

Explain the research area based on the indexed
papers.

==================================================
2. CURRENT STATE OF RESEARCH
==================================================

Summarize what the existing papers have already
investigated.

==================================================
3. IDENTIFIED RESEARCH GAP
==================================================

Explain the potential gap found in the literature.

If the indexed papers do not provide enough
information, say:

"Not specified in the indexed papers."

==================================================
4. RESEARCH OBJECTIVE
==================================================

Provide a clear proposed main objective.

==================================================
5. RESEARCH ROADMAP
==================================================

Create a step-by-step roadmap.

STEP 1 — Literature Review

Explain what should be reviewed.

STEP 2 — Problem Definition

Explain how the research problem should be
defined.

STEP 3 — Dataset / Data Collection

Explain what type of data may be required.

Do not invent a specific dataset unless supported
by the indexed papers.

STEP 4 — Data Preprocessing

Explain possible preprocessing requirements.

STEP 5 — Feature Engineering

Explain possible feature engineering if relevant.

STEP 6 — Model / Method Development

Explain suitable approaches based on the
indexed research.

Clearly identify proposed methods.

STEP 7 — Experimentation

Explain how experiments could be conducted.

STEP 8 — Evaluation

Suggest suitable evaluation metrics.

Clearly identify proposed metrics.

STEP 9 — Result Analysis

Explain what should be analyzed.

STEP 10 — Research Validation

Explain how the proposed approach could be
validated.

STEP 11 — Research Paper Writing

Provide a suggested structure for documenting
the research.

==================================================
6. PROPOSED TECHNOLOGY STACK
==================================================

Suggest suitable technologies.

Clearly label them as:

"Proposed technology"

==================================================
7. EXPECTED OUTCOME
==================================================

Describe possible outcomes.

Do not present them as proven results.

==================================================
8. POSSIBLE CHALLENGES
==================================================

List potential challenges.

==================================================
9. TIMELINE
==================================================

Create a realistic phase-based timeline.

Use:

Phase 1
Phase 2
Phase 3
...

Do not claim that this timeline comes from
the existing papers.

==================================================
10. FINAL RESEARCH ROADMAP
==================================================

Provide a concise roadmap:

Research Gap
        ↓
Objective
        ↓
Data
        ↓
Preprocessing
        ↓
Method
        ↓
Experiment
        ↓
Evaluation
        ↓
Analysis
        ↓
Research Contribution

==================================================
IMPORTANT NOTICE
==================================================

Clearly state:

"This roadmap is a proposed research plan based
on the indexed literature. It does not establish
research novelty or guarantee successful results.
Further literature review and expert validation
are required."
"""

    answer, sources = ask_researchmind(
        roadmap_question
    )

    return answer, sources