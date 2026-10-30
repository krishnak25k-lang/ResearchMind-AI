import json
import os

from src.llm import generate_answer


def generate_paper_profile(paper_text):

    question = """
Analyze this research paper and create a structured
research paper profile.

Return ONLY valid JSON.

Use exactly these fields:

{
    "title": "",
    "research_domain": "",
    "problem_statement": "",
    "objectives": "",
    "methodology": "",
    "dataset": "",
    "technologies": "",
    "key_findings": "",
    "limitations": "",
    "future_work": "",
    "keywords": []
}

Rules:

1. Do not invent information.
2. If information is not available, write "Not specified".
3. Keep answers concise but informative.
4. Keywords must be a JSON list.
"""

    response = generate_answer(
        question,
        paper_text
    )

    response = response.strip()

    # Remove Markdown code block
    if response.startswith("```json"):

        response = response[len("```json"):]

    elif response.startswith("```"):

        response = response[len("```"):]

    if response.endswith("```"):

        response = response[:-3]

    response = response.strip()

    try:

        profile = json.loads(response)

    except json.JSONDecodeError:

        raise ValueError(
            "AI returned invalid JSON.\n\n"
            f"AI Response:\n{response}"
        )

    return profile


def save_paper_profile(
    profile,
    paper_name
):

    os.makedirs(
        "data/profiles",
        exist_ok=True
    )

    # Remove .pdf
    filename = os.path.splitext(
        paper_name
    )[0]

    profile_path = os.path.join(
        "data/profiles",
        filename + ".json"
    )

    with open(
        profile_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            profile,
            file,
            indent=4,
            ensure_ascii=False
        )

    return profile_path


def load_paper_profile(
    paper_name
):

    filename = os.path.splitext(
        paper_name
    )[0]

    profile_path = os.path.join(
        "data/profiles",
        filename + ".json"
    )

    if not os.path.exists(
        profile_path
    ):

        return None

    with open(
        profile_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)