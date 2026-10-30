from src.pdf_loader import extract_text_from_pdf
from src.paper_profile import generate_paper_profile


# ==========================================
# PDF
# ==========================================

pdf_path = "data/papers/paper1.pdf"


# ==========================================
# Extract text
# ==========================================

pages = extract_text_from_pdf(
    pdf_path
)


# ==========================================
# Combine pages
# ==========================================

full_text = ""

for page in pages:

    full_text += (
        f"\n\n"
        f"Page {page['page']}:\n"
        f"{page['text']}"
    )


# ==========================================
# Generate profile
# ==========================================

print("\nGenerating paper profile...\n")

profile = generate_paper_profile(
    full_text
)


# ==========================================
# Display
# ==========================================

print("\n================================")
print("RESEARCH PAPER PROFILE")
print("================================")

print(
    f"\nTitle:\n{profile['title']}"
)

print(
    f"\nResearch Domain:\n"
    f"{profile['research_domain']}"
)

print(
    f"\nProblem:\n"
    f"{profile['problem_statement']}"
)

print(
    f"\nObjectives:\n"
    f"{profile['objectives']}"
)

print(
    f"\nMethodology:\n"
    f"{profile['methodology']}"
)

print(
    f"\nDataset:\n"
    f"{profile['dataset']}"
)

print(
    f"\nTechnologies:\n"
    f"{profile['technologies']}"
)

print(
    f"\nKey Findings:\n"
    f"{profile['key_findings']}"
)

print(
    f"\nLimitations:\n"
    f"{profile['limitations']}"
)

print(
    f"\nFuture Work:\n"
    f"{profile['future_work']}"
)

print(
    f"\nKeywords:\n"
    f"{', '.join(profile['keywords'])}"
)