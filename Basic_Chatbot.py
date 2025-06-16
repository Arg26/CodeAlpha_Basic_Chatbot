import datetime

# Define predefined responses
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Ask me anything.",
    "how are you": "I'm just a program, but I'm doing fine. Thanks!",
    "what's your name": "I'm PyBot, your friendly chatbot assistant.",
    "bye": "Goodbye! Have a great day.",
    "thank you": "You're welcome!",
    "help": "I can respond to greetings, questions, and simple keywords like 'time', 'date', 'bye', etc.",
    "time": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}",
    "date": f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}"
}

# Keep track of the conversation
conversation_history = []

# Function to get response based on input
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm not sure how to respond to that. Try asking something else or type 'help'."

# Function to save the conversation to a file
def save_conversation(history, filename="chat_log.txt"):
    with open(filename, "w") as file:
        file.write("=== ChatBot Conversation Log ===\n")
        for entry in history:
            file.write(entry + "\n")
    print(f"Conversation saved to '{filename}'.")

# Main chatbot loop
def run_chatbot():
    print("👋 Welcome to PyBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            confirm = input("Are you sure you want to exit? (yes/no): ").lower()
            if confirm in ['yes', 'y']:
                print("Bot: Goodbye! 👋")
                break
            else:
                continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        # Store conversation history
        conversation_history.append(f"You: {user_input}")
        conversation_history.append(f"Bot: {response}")

    save_option = input("Do you want to save this conversation? (yes/no): ").lower()
    if save_option in ['yes', 'y']:
        save_conversation(conversation_history)

# Start chatbot
if __name__ == "__main__":
    run_chatbot()
