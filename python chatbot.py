
def chatbot():
    print("🤖 Welcome to AI Chatbot (Type 'bye' to exit)\n")

    bot = {
        "hello": "Hi Supriya! 😊",
        "how are you": "I am fine 👍",
        "what is your name": "I'm AI Chatbot 🤖",
    }

    while True:
        user = input("You: ").lower().strip()

        if user == "bye":
            print("Bot: Goodbye! 👋")
            break

        print("Bot:", bot.get(user, "I don't understand 😅"))

chatbot()
