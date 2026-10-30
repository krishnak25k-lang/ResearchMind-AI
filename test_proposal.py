from src.proposal_generator import generate_research_proposal


print()
print("=" * 70)
print("RESEARCHMIND AI - RESEARCH PROPOSAL GENERATOR")
print("=" * 70)

print()

gap = input(
    "Enter the potential research gap:\n\n"
)

if not gap.strip():

    print(
        "\nPlease enter a research gap."
    )

    exit()


print()
print("🔬 Generating research proposal...")
print()


try:

    answer, sources = generate_research_proposal(
        gap
    )

    print()
    print("=" * 70)
    print("💡 PROPOSED RESEARCH")
    print("=" * 70)

    print()

    print(answer)

    print()
    print("=" * 70)
    print("📚 SUPPORTING SOURCES")
    print("=" * 70)

    if sources:

        seen = set()

        for source in sources:

            if not isinstance(
                source,
                dict
            ):

                continue

            paper = source.get(
                "paper",
                "Unknown Paper"
            )

            page = source.get(
                "page",
                "Unknown"
            )

            key = (
                paper,
                page
            )

            if key not in seen:

                print(
                    f"\n📄 Paper: {paper}"
                )

                print(
                    f"📖 Page: {page}"
                )

                seen.add(key)

    else:

        print(
            "\nNo sources returned."
        )


except Exception as e:

    print()
    print("=" * 70)
    print("❌ ERROR")
    print("=" * 70)

    print()

    print(e)