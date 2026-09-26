from ai_service import ask_ai


def main():
    question = "Hello, introduce yourself in one short sentence."
    answer = ask_ai(question)

    print("AI Response:")
    print(answer)


if __name__ == "__main__":
    main()
