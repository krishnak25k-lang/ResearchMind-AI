from src.research_idea import generate_research_ideas


print("=" * 70)
print("RESEARCHMIND AI - RESEARCH IDEA GENERATOR")
print("=" * 70)


topic = input(
    "\nEnter your research topic: "
)


print("\nGenerating research ideas...\n")


try:

    answer, sources = generate_research_ideas(
        topic
    )

    print("\n")
    print("=" * 70)
    print("RESEARCH IDEA")
    print("=" * 70)

    print("\n")
    print(answer)

    print("\n")
    print("=" * 70)
    print("RESEARCH SOURCES")
    print("=" * 70)

    seen = set()

    for source in sources:

        paper = source.get(
            "paper",
            "Unknown Paper"
        )

        if paper not in seen:

            print(f"\n📄 {paper}")

            seen.add(paper)


except Exception as e:

    print("\n❌ Failed to generate research idea.")

    print(f"\nError: {e}")