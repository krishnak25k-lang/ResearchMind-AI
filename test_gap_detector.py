from src.gap_detector import detect_research_gaps


print()
print("=" * 70)
print("RESEARCHMIND AI - RESEARCH GAP DETECTOR")
print("=" * 70)


question = input(
    "\nWhat research gap do you want to investigate? "
)


if not question.strip():

    print(
        "\nPlease enter a research topic."
    )

    exit()


print()
print("🔬 Analyzing research papers...")
print()


try:

    answer, sources = detect_research_gaps(
        question
    )

    print()
    print("=" * 70)
    print("🔬 POTENTIAL RESEARCH GAPS")
    print("=" * 70)

    print()

    print(answer)

    print()
    print("=" * 70)
    print("📚 SUPPORTING SOURCES")
    print("=" * 70)

    if not sources:

        print(
            "\nNo sources returned."
        )

    else:

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


except Exception as e:

    print()
    print("=" * 70)
    print("❌ ERROR")
    print("=" * 70)

    print()

    print(e)