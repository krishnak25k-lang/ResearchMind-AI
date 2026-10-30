from src.research_report import generate_research_report


print()
print("=" * 70)
print("RESEARCHMIND AI - RESEARCH REPORT GENERATOR")
print("=" * 70)

print()

topic = input(
    "Enter your research topic:\n\n"
)

if not topic.strip():

    print(
        "\n❌ Please enter a research topic."
    )

    exit()


print()
print("📑 Generating research report...")
print()


try:

    answer, sources = generate_research_report(
        topic
    )

    print()
    print("=" * 70)
    print("📑 RESEARCH REPORT")
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

            if not isinstance(source, dict):
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