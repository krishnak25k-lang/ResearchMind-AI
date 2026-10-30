from google import genai
import os

from dotenv import load_dotenv

from src.cache_manager import (
    get_cached_answer,
    store_cached_answer
)


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# API KEY
# ============================================================

API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


if not API_KEY:

    raise ValueError(
        "GEMINI_API_KEY is not set.\n"
        "Please add it to your .env file."
    )


# ============================================================
# GEMINI CLIENT
# ============================================================

client = genai.Client(
    api_key=API_KEY
)


# ============================================================
# MODEL
# ============================================================

MODEL_NAME = "gemini-3.5-flash-lite"


# ============================================================
# GENERATE ANSWER
# ============================================================

def generate_answer(
    question,
    context
):

    """
    Generate answer using:

    1. Persistent cache
    2. Gemini API if cache misses
    """

    # ========================================================
    # CHECK CACHE
    # ========================================================

    cached_answer = get_cached_answer(
        question,
        context
    )


    if cached_answer is not None:

        print(
            "\n[CACHE] Answer found in cache."
        )

        return cached_answer


    # ========================================================
    # CACHE MISS
    # ========================================================

    print(
        "\n[CACHE] No cached answer found."
    )

    print(
        "[GEMINI] Sending request..."
    )


    # ========================================================
    # PROMPT
    # ========================================================

    prompt = f"""
You are ResearchMind AI,
an AI-powered academic research assistant.

Answer the user's question using ONLY
the research-paper context provided below.

IMPORTANT RULES:

1. Do not invent information.
2. Do not use unsupported facts.
3. If information is unavailable, say:

"The information is not specified in the
indexed research papers."

4. Give a clear and technically accurate answer.
5. Use headings and bullet points when useful.
6. Mention relevant papers when possible.

==================================================
USER QUESTION
==================================================

{question}

==================================================
RESEARCH PAPER CONTEXT
==================================================

{context}

==================================================

Provide the final answer.
"""


    # ========================================================
    # CALL GEMINI
    # ========================================================

    try:

        response = client.models.generate_content(

            model=MODEL_NAME,

            contents=prompt
        )


        # ====================================================
        # CHECK RESPONSE
        # ====================================================

        if response is None:

            return (
                "Gemini returned an empty response."
            )


        answer = getattr(
            response,
            "text",
            None
        )


        if not answer:

            return (
                "Gemini returned an empty answer."
            )


        # ====================================================
        # SAVE ANSWER TO CACHE
        # ====================================================

        store_cached_answer(
            question,
            context,
            answer
        )


        print(
            "[CACHE] Answer saved."
        )


        return answer


    # ========================================================
    # ERROR HANDLING
    # ========================================================

    except Exception as e:

        error_text = str(e)


        # ----------------------------------------------------
        # QUOTA ERROR
        # ----------------------------------------------------

        if (
            "429" in error_text
            or
            "RESOURCE_EXHAUSTED" in error_text
            or
            "quota" in error_text.lower()
        ):

            return (
                "⚠️ Gemini API quota exceeded.\n\n"
                "Please check your Gemini API quota "
                "and try again later."
            )


        # ----------------------------------------------------
        # MODEL ERROR
        # ----------------------------------------------------

        if (
            "404" in error_text
            or
            "NOT_FOUND" in error_text
        ):

            return (
                "⚠️ Gemini model is unavailable.\n\n"
                f"Current model: {MODEL_NAME}"
            )


        # ----------------------------------------------------
        # OTHER ERROR
        # ----------------------------------------------------

        return (
            "❌ Failed to generate answer.\n\n"
            f"{error_text}"
        )