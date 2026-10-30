from src.research_roadmap import generate_research_roadmap


print()
print("=" * 70)
print("RESEARCHMIND AI - RESEARCH ROADMAP GENERATOR")
print("=" * 70)

print()

topic = input(
    "Enter your research topic or research gap:\n\n"
)

if not topic.strip():

    print(
        "\nPlease enter a research topic or gap."
    )

    exit()


print()
print("🗺️ Generating research roadmap...")
print()


try:

    answer, sources = generate_research_roadmap(
        topic
    )

    print()
    print("=" * 70)
    print("🗺️ RESEARCH ROADMAP")
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