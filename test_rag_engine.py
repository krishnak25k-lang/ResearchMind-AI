from src.rag import ask_researchmind


question = input(
    "\nAsk ResearchMind AI: "
)


answer, sources = ask_researchmind(
    question
)


print("\n")
print("=" * 70)
print("RESEARCHMIND AI")
print("=" * 70)


print("\nANSWER:")
print(answer)


print("\n")
print("=" * 70)
print("SOURCES")
print("=" * 70)


for i, source in enumerate(
    sources,
    start=1
):

    print(
        f"\n[{i}] "
        f"{source['paper']} "
        f"- Page {source['page']}"
    )