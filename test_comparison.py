from src.comparison import compare_papers


print()
print("=" * 70)
print("RESEARCHMIND AI - MULTI-PAPER COMPARISON")
print("=" * 70)


question = input(
    "\nWhat do you want to compare? "
)


if not question.strip():

    print(
        "\nPlease enter a comparison question."
    )

    exit()


print()
print("🔎 Analyzing research papers...")
print()


try:

    answer, sources = compare_papers(
        question
    )

    print()
    print("=" * 70)
    print("📊 COMPARISON RESULT")
    print("=" * 70)

    print()

    print(answer)

    print()
    print("=" * 70)
    print("📚 RESEARCH SOURCES")
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