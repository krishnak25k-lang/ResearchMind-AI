from src.chat import ask_chat


chat_history = []


print()
print("=" * 70)
print("RESEARCHMIND AI - RESEARCH CHAT")
print("=" * 70)


while True:

    question = input(
        "\nYou: "
    )

    if question.lower() in [
        "exit",
        "quit",
        "q"
    ]:

        print(
            "\nChat ended."
        )

        break

    if not question.strip():

        print(
            "Please enter a question."
        )

        continue


    try:

        answer, sources = ask_chat(
            question,
            chat_history
        )


        print()
        print("-" * 70)
        print("ResearchMind AI:")
        print("-" * 70)

        print(answer)


        # Save conversation
        chat_history.append(
            {
                "role": "user",
                "content": question
            }
        )

        chat_history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


        print()
        print("📚 Sources:")

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
                        f"📄 {paper} | Page: {page}"
                    )

                    seen.add(key)

        else:

            print(
                "No sources returned."
            )


    except Exception as e:

        print()
        print(
            "❌ Error:"
        )

        print(e)