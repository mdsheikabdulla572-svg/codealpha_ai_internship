# chatbot_example.py

def chatbot():
    print("Hello! I am your chatbot 🤖")
    while True:
        user = input("You: ")
        if user.lower() in ["exit", "quit"]:
            print("Bot: Goodbye 👋")
            break
        else:
            print("Bot: You said ->", user)

if __name__ == "__main__":
    chatbot()
