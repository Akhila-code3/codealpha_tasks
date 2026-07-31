def chatbot():
    print("Simple Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: I don't understand that.")
            

# Run the chatbot
chatbot()