from src.rag import ask_researchmind


def ask_chat(question, chat_history=None):
    """
    Ask ResearchMind AI using previous conversation context.
    """

    if chat_history is None:
        chat_history = []

    conversation = ""

    for message in chat_history:

        role = message.get("role", "")
        content = message.get("content", "")

        if role == "user":

            conversation += (
                f"\nUSER:\n{content}\n"
            )

        elif role == "assistant":

            conversation += (
                f"\nASSISTANT:\n{content}\n"
            )

    prompt = f"""
You are ResearchMind AI, an academic research
assistant.

Answer the user's current question using ONLY
the indexed research papers and the conversation
context provided below.

IMPORTANT RULES:

1. Use evidence from the retrieved research papers.
2. Do not invent facts.
3. If the information is not available, say:
   "Not specified in the indexed papers."
4. Keep the answer academically useful.
5. Use previous conversation only to understand
   the user's follow-up question.
6. Do not treat previous AI answers as evidence.
7. Prefer information from the research papers.

==================================================
PREVIOUS CONVERSATION
==================================================

{conversation}

==================================================
CURRENT QUESTION
==================================================

{question}

==================================================

Provide a clear and structured answer.

If appropriate, mention the research paper
supporting the answer.
"""

    answer, sources = ask_researchmind(prompt)

    return answer, sources