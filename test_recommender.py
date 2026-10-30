from src.recommender import recommend_papers


print()
print("=" * 70)
print("RESEARCHMIND AI - PAPER RECOMMENDATION")
print("=" * 70)

print()

topic = input(
    "Enter your research topic:\n\n"
)

if not topic.strip():

    print(
        "\nPlease enter a research topic."
    )

    exit()


print()
print("🔎 Finding relevant research papers...")
print()


try:

    answer, sources = recommend_papers(
        topic
    )

    print()
    print("=" * 70)
    print("📚 RECOMMENDED RESEARCH PAPERS")
    print("=" * 70)

    print()

    print(answer)

    print()
    print("=" * 70)
    print("📖 RESEARCH SOURCES")
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
                    f"\n📄 {paper}"
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