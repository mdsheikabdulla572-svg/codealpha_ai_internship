from deep_translator import GoogleTranslator

print("🤖🌐 Smart AI Chatbot Started!")
print("Type 'exit' to stop\n")

# predefined smart replies
replies = {
    "hi": "வணக்கம் 👋",
    "hello": "வணக்கம் 😊",
    "good morning": "காலை வணக்கம் 🌅",
    "good afternoon": "மதிய வணக்கம் ☀️",
    "good evening": "மாலை வணக்கம் 🌇",
    "how are you": "நீங்கள் எப்படி இருக்கிறீர்கள்?",
    "thank you": "நன்றி 🙏",
    "bye": "பிரியாவிடை 👋"
}

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Goodbye 👋")
        break

    # ✅ direct reply if known
    if user in replies:
        print("Bot:", replies[user])
        continue

    # 🌐 translation fallback
    print("\nChoose language:")
    print("1. Tamil")
    print("2. Hindi")
    print("3. French")

    choice = input("Enter choice: ")

    if choice == "1":
        lang = "ta"
        name = "Tamil"
    elif choice == "2":
        lang = "hi"
        name = "Hindi"
    elif choice == "3":
        lang = "fr"
        name = "French"
    else:
        print("Invalid choice 😅\n")
        continue

    try:
        translated = GoogleTranslator(source='auto', target=lang).translate(user)
        print(f"Bot ({name}): {translated}\n")
    except:
        print("Error 😓")