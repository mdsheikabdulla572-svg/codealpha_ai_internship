print("🤖 I am AI Chat Bot ✨ (type 'exit' to stop)")

memory = []

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Goodbye 👋")
        break

    memory.append(user)

    # Greetings
    if "hi" in user or "hello" in user:
        print("Bot: Hello 👋 How are you?")

    elif "how are you" in user:
        print("Bot: I'm doing great 😎 How about you?")

    elif "i am fine" in user or "i'm fine" in user:
        print("Bot: That's nice to hear 😊 What do you want to talk about?")

    # Memory
    elif "what did i say" in user:
        if len(memory) > 1:
            print("Bot: You said:", memory[-2])
        else:
            print("Bot: You didn't say anything before 😅")

    # Main Questions
    elif "what is python" in user:
        print("Bot: Python is a powerful and easy programming language 🐍.")

    elif "what is ai" in user:
        print("Bot: AI means machines can think and learn like humans 🤖.")

    elif "how many countries" in user:
        print("Bot: There are about 195 countries in the world 🌍.")

    # Extra Knowledge
    elif "what is computer" in user:
        print("Bot: A computer is an electronic machine that processes data 💻.")

    elif "who created python" in user:
        print("Bot: Python was created by Guido van Rossum 👨‍💻.")

    elif "what is internet" in user:
        print("Bot: The internet connects millions of computers worldwide 🌐.")

    elif "what is coding" in user:
        print("Bot: Coding means giving instructions to a computer 🧠.")

    elif "what is chatbot" in user:
        print("Bot: A chatbot is a program that talks with humans 😎.")

    elif "what is machine learning" in user:
        print("Bot: Machine Learning is a part of AI that learns from data 📊.")

    elif "who are you" in user or "your name" in user:
        print("Bot: I am AI Chat Bot ✨ created using Python 😎.")

    # Fun
    elif "thank" in user:
        print("Bot: You're welcome 😊")

    elif "bouquet" in user:
        print("Bot: 💐")

    elif "emoji" in user:
        print("Bot: 😎🔥✨💯")

    elif "motivation" in user:
        print("Bot: Never give up 💪 Consistency is the key to success ✨")

    elif "bye" in user:
        print("Bot: Bye 👋 Have a great day!")
        break

    # Smart fallback (conversation feel)
    else:
        print("Bot: That's interesting 🤔 Tell me more about it!")