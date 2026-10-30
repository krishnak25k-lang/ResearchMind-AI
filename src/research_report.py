from src.rag import ask_researchmind


def generate_research_report(topic):
    """
    Generate a structured research report
    based on the indexed research papers.
    """

    prompt = f"""
You are ResearchMind AI, an academic research
report generation assistant.

The researcher is interested in:

==================================================
RESEARCH TOPIC
==================================================

{topic}

==================================================

Analyze the indexed research papers and create
a structured academic research report.

IMPORTANT RULES:

1. Use evidence from the retrieved research papers.
2. Do not invent information about the papers.
3. If information is unavailable, write:
   "Not specified in the indexed papers."
4. Clearly distinguish existing research from
   proposed research.
5. Do not claim that the proposed research is novel.
6. The report should be useful for a student
   preparing a research project or paper.

Create the report using the following structure:

==================================================
1. ABSTRACT
==================================================

Provide a concise summary of the research area,
existing research and possible research direction.

==================================================
2. INTRODUCTION
==================================================

Explain the research area and why it is important
based on the indexed literature.

==================================================
3. EXISTING RESEARCH
==================================================

Summarize what the indexed research papers have
already investigated.

Mention:

- Research problems
- Methods
- Technologies
- Datasets
- Major findings

==================================================
4. PROBLEM STATEMENT
==================================================

Explain the research problem identified from
the literature.

==================================================
5. RESEARCH GAP
==================================================

Identify potential research gaps based only on:

- Limitations
- Missing approaches
- Future work
- Differences between papers

If there is insufficient evidence, say so.

==================================================
6. RESEARCH OBJECTIVES
==================================================

Provide possible research objectives.

Clearly label these as:

PROPOSED OBJECTIVES

==================================================
7. PROPOSED METHODOLOGY
==================================================

Describe a possible methodology.

Include:

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Model / Algorithm
5. Training
6. Testing
7. Evaluation

Clearly identify proposed methods.

==================================================
8. PROPOSED TECHNOLOGY STACK
==================================================

Suggest suitable technologies.

For example:

- Programming Language
- Framework
- Machine Learning Libraries
- Database
- Visualization
- Deployment

Clearly label them as:

PROPOSED TECHNOLOGIES

==================================================
9. EXPECTED RESULTS
==================================================

Describe possible expected outcomes.

Do not present expected outcomes as
already achieved results.

==================================================
10. LIMITATIONS
==================================================

Discuss limitations found in the existing
research papers.

==================================================
11. FUTURE WORK
==================================================

Summarize future research directions mentioned
in the indexed papers.

Then identify possible future directions
for the proposed research.

Clearly distinguish:

Existing Paper Future Work

and

Proposed Future Work

==================================================
12. CONCLUSION
==================================================

Provide a concise conclusion connecting:

Existing Research
        ↓
Research Gap
        ↓
Proposed Research
        ↓
Expected Contribution

==================================================
13. RESEARCH CONTRIBUTION
==================================================

Explain what the proposed research could
potentially contribute.

Do not claim guaranteed novelty.

==================================================
IMPORTANT
==================================================

End the report with:

"This report is generated from the indexed
research literature. Proposed research directions
require further literature review, experimentation,
and expert validation before claiming novelty
or research contribution."
"""

    answer, sources = ask_researchmind(prompt)

    return answer, sources