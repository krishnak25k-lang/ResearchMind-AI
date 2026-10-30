import os
import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ResearchMind AI",
    page_icon="🔬",
    layout="wide"
)


# ============================================================
# IMPORTS
# ============================================================

from src.rag import ask_researchmind
from src.chat import ask_chat
from src.comparison import compare_papers
from src.gap_detector import detect_research_gaps
from src.recommender import recommend_papers

from src.vector_store import (
    get_all_metadata,
    get_all_papers
)


# ============================================================
# SESSION STATE
# ============================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {
        "New Chat": []
    }

if "selected_papers" not in st.session_state:
    st.session_state.selected_papers = []


# ============================================================
# HELPER - DISPLAY SOURCES
# ============================================================

def display_sources(sources):

    if not sources:
        return

    st.markdown("---")

    st.subheader("📚 Research Sources")

    seen = set()

    for source in sources:

        if not isinstance(source, dict):
            continue

        paper = source.get(
            "paper",
            source.get(
                "source",
                "Unknown Paper"
            )
        )

        page = source.get(
            "page",
            ""
        )

        text = f"📄 {paper}"

        if page:
            text += f" — Page {page}"

        if text not in seen:

            st.write(text)

            seen.add(text)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🔬 ResearchMind AI")

st.sidebar.markdown("---")


# ============================================================
# UPLOAD RESEARCH PAPER
# ============================================================

st.sidebar.subheader("📤 Add Research Paper")

uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF",
    type=["pdf"],
    key="research_pdf_uploader"
)


if uploaded_file is not None:

    st.sidebar.success(
        f"Selected: {uploaded_file.name}"
    )

    if st.sidebar.button(
        "🚀 Add to ResearchMind",
        key="add_research_paper"
    ):

        try:

            os.makedirs(
                "data/papers",
                exist_ok=True
            )

            save_path = os.path.join(
                "data/papers",
                uploaded_file.name
            )

            with open(
                save_path,
                "wb"
            ) as file:

                file.write(
                    uploaded_file.getbuffer()
                )

            # ------------------------------------------------
            # INDEX PAPER
            # ------------------------------------------------

            try:

                from src.paper_indexer import index_uploaded_paper

                with st.spinner(
                    "📚 Indexing research paper..."
                ):

                    result = index_uploaded_paper(
                        save_path,
                        uploaded_file.name
                    )

                st.sidebar.success(
                    "✅ Paper indexed successfully!"
                )

                if isinstance(result, dict):

                    if "pages" in result:

                        st.sidebar.write(
                            f"📄 Pages: {result['pages']}"
                        )

                    if "chunks" in result:

                        st.sidebar.write(
                            f"🧩 Chunks: {result['chunks']}"
                        )

            except ImportError:

                st.sidebar.warning(
                    "⚠️ Paper saved, but the "
                    "indexing function was not found."
                )

        except Exception as e:

            st.sidebar.error(
                "❌ Failed to upload paper."
            )

            st.sidebar.exception(e)


# ============================================================
# RESEARCH PAPER SELECTION
# ============================================================

st.sidebar.markdown("---")

st.sidebar.subheader(
    "📚 Research Papers"
)

try:

    available_papers = get_all_papers()

    if available_papers:

        st.sidebar.caption(
            "Select the papers you want ResearchMind "
            "to analyze."
        )

        selected_papers = st.sidebar.multiselect(
            "Select Papers",
            options=available_papers,
            default=st.session_state.selected_papers,
            key="paper_selector"
        )

        if st.sidebar.button(
            "🔬 Analyze Selected Papers",
            key="analyze_selected_papers"
        ):

            if not selected_papers:

                st.sidebar.warning(
                    "⚠️ Please select at least one paper."
                )

            else:

                st.session_state.selected_papers = (
                    selected_papers
                )

                st.sidebar.success(
                    f"✅ {len(selected_papers)} "
                    f"paper(s) selected."
                )

                st.rerun()

        # ----------------------------------------------------
        # CURRENT SELECTION
        # ----------------------------------------------------

        if st.session_state.selected_papers:

            st.sidebar.markdown(
                "**Currently analyzing:**"
            )

            for paper in (
                st.session_state.selected_papers
            ):

                st.sidebar.write(
                    f"☑ {paper}"
                )

        else:

            st.sidebar.info(
                "No papers selected. "
                "Select papers to analyze."
            )

    else:

        st.sidebar.info(
            "📭 No indexed papers found."
        )

except Exception as e:

    st.sidebar.error(
        "❌ Could not load research papers."
    )

    st.sidebar.exception(e)


# ============================================================
# CLEAR PAPER SELECTION
# ============================================================

if st.session_state.selected_papers:

    if st.sidebar.button(
        "❌ Clear Paper Selection",
        key="clear_paper_selection"
    ):

        st.session_state.selected_papers = []

        st.rerun()


# ============================================================
# RESEARCH TOOLS
# ============================================================

st.sidebar.markdown("---")

st.sidebar.subheader(
    "🛠️ Research Tools"
)


selected_feature = st.sidebar.selectbox(
    "Select Feature",
    [
        "💬 Ask Research",
        "🧠 Research Chat",
        "📊 Compare Papers",
        "🔬 Research Gap Detection",
        "💡 Research Proposal",
        "🔎 Paper Recommendation",
        "🗺️ Research Roadmap",
        "📑 Research Report",
        "🧠 Research Idea Generator",
        "📝 Automatic Literature Review",
        "📊 Analytics Dashboard"
    ],
    key="research_feature"
)


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🔬 ResearchMind AI")

st.subheader(
    "AI-Powered Research Assistant"
)

st.write(
    """
ResearchMind AI combines:

**RAG + Semantic Search + Research Analysis +
Multi-Paper Comparison + Research Gap Detection +
Proposal Generation + Paper Recommendation +
Research Roadmap + Research Report +
Research Chat + Research Idea Generation +
Automatic Literature Review + Analytics**
"""
)


# ============================================================
# SELECTED PAPER STATUS
# ============================================================

if st.session_state.selected_papers:

    st.info(
        "🔬 Currently analyzing: "
        + ", ".join(
            st.session_state.selected_papers
        )
    )

else:

    st.warning(
        "📚 No papers selected. "
        "Select papers from the sidebar before "
        "performing paper-specific analysis."
    )


st.markdown("---")


# ============================================================
# 1. ASK RESEARCH
# ============================================================

if selected_feature == "💬 Ask Research":

    st.header(
        "💬 Ask ResearchMind AI"
    )

    question = st.text_area(
        "Enter your research question",
        placeholder=(
            "Example: What methodology is used "
            "in these research papers?"
        ),
        height=120,
        key="ask_question"
    )

    if st.button(
        "🔍 Ask ResearchMind",
        key="ask_button"
    ):

        if not question.strip():

            st.warning(
                "⚠️ Please enter a question."
            )

        elif not st.session_state.selected_papers:

            st.warning(
                "⚠️ Please select at least one "
                "research paper from the sidebar."
            )

        else:

            try:

                with st.spinner(
                    "🔎 Searching selected papers..."
                ):

                    answer, sources = ask_researchmind(
                        question,
                        selected_papers=(
                            st.session_state.selected_papers
                        )
                    )

                st.success(
                    "✅ Answer generated!"
                )

                st.subheader(
                    "💬 Answer"
                )

                st.markdown(answer)

                display_sources(
                    sources
                )

            except Exception as e:

                st.error(
                    "❌ Failed to generate answer."
                )

                st.exception(e)


# ============================================================
# 2. RESEARCH CHAT
# ============================================================

elif selected_feature == "🧠 Research Chat":

    st.header(
        "🧠 Research Chat"
    )

    st.write(
        "Have a continuous conversation with ResearchMind AI."
    )

    chat_names = list(
        st.session_state.chat_sessions.keys()
    )

    selected_chat_name = st.sidebar.selectbox(
        "Select Chat",
        chat_names,
        key="chat_selection"
    )

    st.session_state.chat_history = (
        st.session_state.chat_sessions[
            selected_chat_name
        ]
    )

    # --------------------------------------------------------
    # CHAT HISTORY
    # --------------------------------------------------------

    for message in st.session_state.chat_history:

        role = message.get(
            "role",
            ""
        )

        content = message.get(
            "content",
            ""
        )

        if role == "user":

            with st.chat_message("user"):

                st.write(content)

        elif role == "assistant":

            with st.chat_message("assistant"):

                st.write(content)

    chat_question = st.chat_input(
        "Ask ResearchMind something..."
    )

    if chat_question:

        if not st.session_state.selected_papers:

            st.warning(
                "⚠️ Please select research papers first."
            )

        else:

            with st.chat_message("user"):

                st.write(
                    chat_question
                )

            try:

                with st.chat_message(
                    "assistant"
                ):

                    with st.spinner(
                        "Thinking..."
                    ):

                        answer, sources = ask_chat(
                            chat_question,
                            st.session_state.chat_history,
                            st.session_state.selected_papers
                        )

                    st.write(
                        answer
                    )

                st.session_state.chat_history.append(
                    {
                        "role": "user",
                        "content": chat_question
                    }
                )

                st.session_state.chat_history.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

                st.session_state.chat_sessions[
                    selected_chat_name
                ] = st.session_state.chat_history

            except Exception as e:

                st.error(
                    "❌ Failed to generate chat response."
                )

                st.exception(e)

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🗑️ Clear Current Chat",
            key="clear_chat"
        ):

            st.session_state.chat_sessions[
                selected_chat_name
            ] = []

            st.session_state.chat_history = []

            st.rerun()

    with col2:

        if st.button(
            "➕ New Chat",
            key="new_chat"
        ):

            chat_number = len(
                st.session_state.chat_sessions
            )

            new_name = (
                f"Chat {chat_number}"
            )

            st.session_state.chat_sessions[
                new_name
            ] = []

            st.rerun()


# ============================================================
# 3. COMPARE PAPERS
# ============================================================

elif selected_feature == "📊 Compare Papers":

    st.header(
        "📊 Research Paper Comparison"
    )

    question = st.text_area(
        "What do you want to compare?",
        placeholder=(
            "Example: Compare the methodologies "
            "used in the selected papers."
        ),
        height=120,
        key="compare_question"
    )

    if st.button(
        "📊 Compare Papers",
        key="compare_button"
    ):

        if not question.strip():

            st.warning(
                "⚠️ Please enter a comparison question."
            )

        elif not st.session_state.selected_papers:

            st.warning(
                "⚠️ Select papers first."
            )

        else:

            try:

                with st.spinner(
                    "📊 Comparing selected papers..."
                ):

                    answer, sources = ask_researchmind(
                        question,
                        selected_papers=(
                            st.session_state.selected_papers
                        )
                    )

                st.success(
                    "✅ Comparison completed!"
                )

                st.markdown(
                    answer
                )

                display_sources(
                    sources
                )

            except Exception as e:

                st.error(
                    "❌ Failed to compare papers."
                )

                st.exception(e)


# ============================================================
# 4. RESEARCH GAP DETECTION
# ============================================================

elif selected_feature == "🔬 Research Gap Detection":

    st.header(
        "🔬 Research Gap Detection"
    )

    topic = st.text_area(
        "Enter research topic",
        placeholder=(
            "Example: AI in Healthcare"
        ),
        height=120,
        key="gap_topic"
    )

    if st.button(
        "🔬 Detect Research Gaps",
        key="gap_button"
    ):

        if not topic.strip():

            st.warning(
                "⚠️ Please enter a research topic."
            )

        elif not st.session_state.selected_papers:

            st.warning(
                "⚠️ Select papers first."
            )

        else:

            prompt = f"""
Analyze the research gaps related to:

{topic}

Use ONLY the selected indexed research papers.

Identify:

1. Existing Research
2. Common Approaches
3. Limitations
4. Missing Areas
5. Research Gaps
6. Possible Future Research
"""

            try:

                with st.spinner(
                    "🔎 Detecting research gaps..."
                ):

                    answer, sources = ask_researchmind(
                        prompt,
                        selected_papers=(
                            st.session_state.selected_papers
                        )
                    )

                st.success(
                    "✅ Research gap detection completed!"
                )

                st.markdown(
                    answer
                )

                display_sources(
                    sources
                )

            except Exception as e:

                st.error(
                    "❌ Failed to detect research gaps."
                )

                st.exception(e)


# ============================================================
# 5. RESEARCH PROPOSAL
# ============================================================

elif selected_feature == "💡 Research Proposal":

    st.header(
        "💡 Research Proposal Generator"
    )

    topic = st.text_area(
        "Enter your research topic",
        placeholder=(
            "Example: AI-based disease prediction"
        ),
        height=120,
        key="proposal_topic"
    )

    if st.button(
        "💡 Generate Proposal",
        key="proposal_button"
    ):

        if not topic.strip():

            st.warning(
                "⚠️ Please enter a research topic."
            )

        elif not st.session_state.selected_papers:

            st.warning(
                "⚠️ Select papers first."
            )

        else:

            prompt = f"""
Generate a structured research proposal for:

{topic}

Use ONLY the selected research papers.

Do not invent facts.

Include:

1. Proposed Title
2. Research Area
3. Background
4. Existing Research
5. Research Gap
6. Problem Statement
7. Objectives
8. Proposed Methodology
9. Technologies / Algorithms
10. Possible Dataset
11. Expected Results
12. Expected Contribution
13. Limitations
14. Future Scope
"""

            try:

                with st.spinner(
                    "💡 Generating proposal..."
                ):

                    answer, sources = ask_researchmind(
                        prompt,
                        selected_papers=(
                            st.session_state.selected_papers
                        )
                    )

                st.success(
                    "✅ Proposal generated!"
                )

                st.markdown(
                    answer
                )

                display_sources(
                    sources
                )

            except Exception as e:

                st.error(
                    "❌ Failed to generate proposal."
                )

                st.exception(e)


# ============================================================
# 6. PAPER RECOMMENDATION
# ============================================================

elif selected_feature == "🔎 Paper Recommendation":

    st.header(
        "🔎 Paper Recommendation"
    )

    topic = st.text_area(
        "Enter research topic",
        placeholder=(
            "Example: Large Language Models in Education"
        ),
        height=120,
        key="recommendation_topic"
    )

    if st.button(
        "🔎 Recommend Papers",
        key="recommend_button"
    ):

        if not topic.strip():

            st.warning(
                "⚠️ Please enter a research topic."
            )

        elif not st.session_state.selected_papers:

            st.warning(
                "⚠️ Select papers first."
            )

        else:

            prompt = f"""
Recommend the most relevant papers from the
selected research papers for this topic:

{topic}

Explain why each selected paper is relevant.
Use ONLY information from the selected papers.
"""

            try:

                with st.spinner(
                    "🔎 Finding relevant papers..."
                ):

                    answer, sources = ask_researchmind(
                        prompt,
                        selected_papers=(
                            st.session_state.selected_papers
                        )
                    )

                st.success(
                    "✅ Recommendations generated!"
                )

                st.markdown(
                    answer
                )

                display_sources(
                    sources
                )

            except Exception as e:

                st.error(
                    "❌ Failed to recommend papers."
                )

                st.exception(e)


# ============================================================
# 7. RESEARCH ROADMAP
# ============================================================

elif selected_feature == "🗺️ Research Roadmap":

    st.header(
        "🗺️ Research Roadmap"
    )

    topic = st.text_area(
        "Enter research topic",
        placeholder=(
            "Example: AI Student Performance Prediction"
        ),
        height=120,
        key="roadmap_topic"
    )

    if st.button(
        "🗺️ Generate Roadmap",
        key="roadmap_button"
    ):

        if not topic.strip():

            st.warning(
                "⚠️ Please enter a research topic."
            )

        elif not st.session_state.selected_papers:

            st.warning(
                "⚠️ Select papers first."
            )

        else:

            prompt = f"""
Create a research roadmap for:

{topic}

Use ONLY information from the selected research papers.

Include:

1. Research Topic
2. Problem Definition
3. Literature Review
4. Research Gap
5. Objectives
6. Dataset Collection
7. Data Preprocessing
8. Proposed Methodology
9. Model Development
10. Experimentation
11. Evaluation
12. Results Analysis
13. Paper Writing
14. Future Improvements
"""

            try:

                with st.spinner(
                    "🗺️ Creating research roadmap..."
                ):

                    answer, sources = ask_researchmind(
                        prompt,
                        selected_papers=(
                            st.session_state.selected_papers
                        )
                    )

                st.success(
                    "✅ Roadmap generated!"
                )

                st.markdown(
                    answer
                )

                display_sources(
                    sources
                )

            except Exception as e:

                st.error(
                    "❌ Failed to generate roadmap."
                )

                st.exception(e)


# ============================================================
# 8. RESEARCH REPORT
# ============================================================

elif selected_feature == "📑 Research Report":

    st.header(
        "📑 Research Report Generator"
    )

    topic = st.text_area(
        "Enter research topic",
        placeholder=(
            "Example: Machine Learning in Education"
        ),
        height=120,
        key="report_topic"
    )

    if st.button(
        "📑 Generate Report",
        key="report_button"
    ):

        if not topic.strip():

            st.warning(
                "⚠️ Please enter a research topic."
            )

        elif not st.session_state.selected_papers:

            st.warning(
                "⚠️ Select papers first."
            )

        else:

            prompt = f"""
Prepare a structured research report about:

{topic}

Use ONLY evidence retrieved from the selected
research papers.

Do not invent information.

Include:

1. Research Topic
2. Introduction
3. Existing Research
4. Research Problem
5. Research Objectives
6. Methodologies Used
7. Datasets
8. Technologies and Algorithms
9. Key Findings
10. Comparison
11. Research Gaps
12. Limitations
13. Future Research Directions
14. Conclusion
"""

            try:

                with st.spinner(
                    "📑 Generating report..."
                ):

                    answer, sources = ask_researchmind(
                        prompt,
                        selected_papers=(
                            st.session_state.selected_papers
                        )
                    )

                st.success(
                    "✅ Report generated!"
                )

                st.markdown(
                    answer
                )

                display_sources(
                    sources
                )

                st.download_button(
                    "📄 Download Research Report",
                    data=answer,
                    file_name="research_report.txt",
                    mime="text/plain",
                    key="download_report"
                )

            except Exception as e:

                st.error(
                    "❌ Failed to generate report."
                )

                st.exception(e)


# ============================================================
# 9. RESEARCH IDEA GENERATOR
# ============================================================

elif selected_feature == "🧠 Research Idea Generator":

    st.header(
        "🧠 Research Idea Generator"
    )

    topic = st.text_area(
        "Enter research topic",
        placeholder=(
            "Example: Artificial Intelligence in Healthcare"
        ),
        height=120,
        key="idea_topic"
    )

    if st.button(
        "🧠 Generate Research Idea",
        key="idea_button"
    ):

        if not topic.strip():

            st.warning(
                "⚠️ Please enter a research topic."
            )

        elif not st.session_state.selected_papers:

            st.warning(
                "⚠️ Select papers first."
            )

        else:

            prompt = f"""
You are ResearchMind AI.

Generate a new research idea related to:

{topic}

Analyze ONLY the selected research papers.

Use their research gaps, limitations and future work.

Do not invent research findings.

Create:

1. Research Area
2. Existing Research
3. Identified Research Gap
4. Proposed Research Idea
5. Proposed Title
6. Problem Statement
7. Research Objectives
8. Proposed Methodology
9. Technologies / Algorithms
10. Possible Dataset
11. Expected Contribution
12. Future Scope

Then provide:

RESEARCH IDEA SUMMARY
"""

            try:

                with st.spinner(
                    "🧠 Generating research idea..."
                ):

                    answer, sources = ask_researchmind(
                        prompt,
                        selected_papers=(
                            st.session_state.selected_papers
                        )
                    )

                st.success(
                    "✅ Research idea generated!"
                )

                st.markdown(
                    answer
                )

                display_sources(
                    sources
                )

                st.download_button(
                    "📄 Download Research Idea",
                    data=answer,
                    file_name="research_idea.txt",
                    mime="text/plain",
                    key="download_idea"
                )

            except Exception as e:

                st.error(
                    "❌ Failed to generate research idea."
                )

                st.exception(e)


# ============================================================
# 10. AUTOMATIC LITERATURE REVIEW
# ============================================================

elif selected_feature == "📝 Automatic Literature Review":

    st.header(
        "📝 Automatic Literature Review"
    )

    topic = st.text_area(
        "Enter literature review topic",
        placeholder=(
            "Example: Artificial Intelligence in Healthcare"
        ),
        height=120,
        key="literature_topic"
    )

    if st.button(
        "📝 Generate Literature Review",
        key="literature_button"
    ):

        if not topic.strip():

            st.warning(
                "⚠️ Please enter a topic."
            )

        elif not st.session_state.selected_papers:

            st.warning(
                "⚠️ Select papers first."
            )

        else:

            prompt = f"""
You are ResearchMind AI.

Generate a structured literature review about:

{topic}

Use ONLY evidence from the selected research papers.

Do not invent information.

Structure:

# AUTOMATIC LITERATURE REVIEW

## 1. Research Background

## 2. Existing Research

## 3. Paper-wise Literature Summary

## 4. Methodology Comparison

## 5. Dataset Comparison

## 6. Key Findings

## 7. Common Research Themes

## 8. Differences Between Studies

## 9. Research Gaps

## 10. Limitations

## 11. Future Research Directions

## 12. Overall Literature Analysis

## 13. Research Opportunity

## 14. Conclusion
"""

            try:

                with st.spinner(
                    "📚 Generating literature review..."
                ):

                    answer, sources = ask_researchmind(
                        prompt,
                        selected_papers=(
                            st.session_state.selected_papers
                        )
                    )

                st.success(
                    "✅ Literature review generated!"
                )

                st.markdown(
                    answer
                )

                display_sources(
                    sources
                )

                st.download_button(
                    "📄 Download Literature Review",
                    data=answer,
                    file_name="literature_review.txt",
                    mime="text/plain",
                    key="download_literature"
                )

            except Exception as e:

                st.error(
                    "❌ Failed to generate literature review."
                )

                st.exception(e)


# ============================================================
# 11. ANALYTICS DASHBOARD
# ============================================================

elif selected_feature == "📊 Analytics Dashboard":

    st.header(
        "📊 Research Analytics Dashboard"
    )

    st.write(
        "Statistics from your ChromaDB research knowledge base."
    )

    if st.button(
        "🔄 Refresh Analytics",
        key="analytics_refresh"
    ):

        st.rerun()

    try:

        results = get_all_metadata()

        if results is None:

            st.warning(
                "⚠️ No data returned from ChromaDB."
            )

        else:

            metadatas = results.get(
                "metadatas",
                []
            )

            metadatas = [
                item
                for item in metadatas
                if item
            ]

            total_chunks = len(
                metadatas
            )

            paper_chunks = {}

            paper_pages = {}

            for metadata in metadatas:

                paper = metadata.get(
                    "paper",
                    "Unknown Paper"
                )

                page = metadata.get(
                    "page"
                )

                if paper not in paper_chunks:

                    paper_chunks[paper] = 0

                paper_chunks[paper] += 1

                if paper not in paper_pages:

                    paper_pages[paper] = set()

                if page is not None:

                    paper_pages[paper].add(
                        str(page)
                    )

            total_papers = len(
                paper_chunks
            )

            total_pages = sum(
                len(pages)
                for pages in paper_pages.values()
            )

            if total_papers > 0:

                average_pages = (
                    total_pages /
                    total_papers
                )

            else:

                average_pages = 0

            # ------------------------------------------------
            # METRICS
            # ------------------------------------------------

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(
                    "📚 Total Papers",
                    total_papers
                )

            with col2:

                st.metric(
                    "🧩 Total Chunks",
                    total_chunks
                )

            with col3:

                st.metric(
                    "📄 Total Pages",
                    total_pages
                )

            with col4:

                st.metric(
                    "📑 Average Pages",
                    f"{average_pages:.1f}"
                )

            st.markdown("---")

            # ------------------------------------------------
            # SELECTED PAPER ANALYTICS
            # ------------------------------------------------

            st.subheader(
                "🔬 Current Analysis"
            )

            selected_count = len(
                st.session_state.selected_papers
            )

            st.metric(
                "Selected Papers",
                selected_count
            )

            if st.session_state.selected_papers:

                st.write(
                    "Currently selected:"
                )

                for paper in (
                    st.session_state.selected_papers
                ):

                    st.write(
                        f"☑ {paper}"
                    )

            else:

                st.info(
                    "No papers are currently selected."
                )

            st.markdown("---")

            # ------------------------------------------------
            # PAPER DETAILS
            # ------------------------------------------------

            st.subheader(
                "📚 Indexed Research Papers"
            )

            if total_papers == 0:

                st.info(
                    "No research papers are indexed."
                )

            else:

                for paper in sorted(
                    paper_chunks.keys()
                ):

                    chunks = paper_chunks[
                        paper
                    ]

                    pages = len(
                        paper_pages.get(
                            paper,
                            set()
                        )
                    )

                    with st.expander(
                        f"📄 {paper}"
                    ):

                        c1, c2 = st.columns(2)

                        with c1:

                            st.metric(
                                "🧩 Chunks",
                                chunks
                            )

                        with c2:

                            st.metric(
                                "📄 Pages",
                                pages
                            )

            st.markdown("---")

            # ------------------------------------------------
            # CHUNKS CHART
            # ------------------------------------------------

            if paper_chunks:

                st.subheader(
                    "🧩 Chunks per Paper"
                )

                chunk_chart = {
                    paper: paper_chunks[paper]
                    for paper in sorted(
                        paper_chunks.keys()
                    )
                }

                st.bar_chart(
                    chunk_chart
                )

            st.markdown("---")

            # ------------------------------------------------
            # PAGES CHART
            # ------------------------------------------------

            if paper_pages:

                st.subheader(
                    "📄 Pages per Paper"
                )

                page_chart = {
                    paper: len(
                        paper_pages[paper]
                    )
                    for paper in sorted(
                        paper_pages.keys()
                    )
                }

                st.bar_chart(
                    page_chart
                )

            st.markdown("---")

            # ------------------------------------------------
            # DATABASE INFORMATION
            # ------------------------------------------------

            st.subheader(
                "🗄️ Database Information"
            )

            c1, c2 = st.columns(2)

            with c1:

                st.write(
                    "**Vector Database:** ChromaDB"
                )

                st.write(
                    "**Collection:** research_papers"
                )

                st.write(
                    f"**Indexed Papers:** {total_papers}"
                )

            with c2:

                st.write(
                    f"**Stored Chunks:** {total_chunks}"
                )

                st.write(
                    f"**Unique Pages:** {total_pages}"
                )

                st.write(
                    "**Metadata:** paper, page"
                )

    except Exception as e:

        st.error(
            "❌ Failed to load Analytics Dashboard."
        )

        st.exception(e)


# ============================================================
# SIDEBAR FOOTER
# ============================================================

st.sidebar.markdown("---")

st.sidebar.caption(
    "🔬 ResearchMind AI"
)

st.sidebar.caption(
    "AI-Powered Research Assistant"
)