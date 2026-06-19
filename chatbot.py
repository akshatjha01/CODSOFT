print("===================================")
print("     CODSOFT AI CHATBOT")
print("===================================")
print("Type 'bye' to exit\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user == "your name":
        print("Bot: My name is CodSoft AI Chatbot.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "what is machine learning":
        print("Bot: Machine Learning is a branch of AI that enables systems to learn from data.")

    elif user == "good morning":
        print("Bot: Good Morning! Have a wonderful day.")

    elif user == "good night":
        print("Bot: Good Night! Sweet dreams.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "help":
        print("Bot: You can ask me about AI, Machine Learning, greetings, or my name.")

    elif user == "who created you":
        print("Bot: I was created as a CodSoft AI Internship project.")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")