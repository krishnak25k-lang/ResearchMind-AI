import os

from src.pdf_loader import extract_text_from_pdf
from src.paper_profile import (
    generate_paper_profile,
    save_paper_profile,
    load_paper_profile
)


def get_paper_profile(paper_path):

    paper_name = os.path.basename(
        paper_path
    )

    # ==========================================
    # Check if profile already exists
    # ==========================================

    existing_profile = load_paper_profile(
        paper_name
    )

    if existing_profile is not None:

        return existing_profile


    # ==========================================
    # Extract PDF
    # ==========================================

    pages = extract_text_from_pdf(
        paper_path
    )

    full_text = ""

    for page in pages:

        full_text += (
            f"\n\n"
            f"Page {page['page']}:\n"
            f"{page['text']}"
        )


    # ==========================================
    # Generate AI profile
    # ==========================================

    profile = generate_paper_profile(
        full_text
    )


    # ==========================================
    # Save profile
    # ==========================================

    save_paper_profile(
        profile,
        paper_name
    )


    return profile