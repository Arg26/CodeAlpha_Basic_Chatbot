import datetime

# Define predefined responses 
responses = {
    # Say hello
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Ask me anything.",
    "how are you": "I'm just a program, but I'm doing fine. Thanks!",
    "bye": "Goodbye! Have a great day.",
    "thank you": "You're welcome!",
    
    # Time/date
    "time": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}",
    "date": f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}",
    
    # Help/what it does
    "help": "I can respond to greetings, jokes, time, date, weather, and other simple keywords.",
    "what can you do": "I can chat with you, tell jokes, remember our conversation, and more!",

    # Identity
    "what's your name": "I'm PyBot, your friendly chatbot assistant.",
    "who are you": "I'm PyBot, your virtual assistant powered by Python.",
    "are you a robot": "Sort of! I'm a chatbot built with code, not circuits.",
    "who created you": "I was created by a Python programmer like you!",
    "how old are you": "I'm as old as the last time the code was updated!",
    "do you sleep": "Nope, I’m always running... unless you close me!",

    # Have fun
    "tell me a joke": "Why did the programmer quit his job? Because he didn't get arrays!",
    "joke": "Why do Python programmers wear glasses? Because they can't C!",
    "bored": "Let's play a game! Ask me a riddle or type 'joke'!",
    "sing": "I'm better with code than chords, but here's one: ♪ beep boop beep ♪",

    # Weather
    "weather": "I'm not connected to live weather APIs yet, but I hope it's sunny where you are!",
    "how's the weather": "Cloudy with a chance of code!",
    "how do you feel": "I feel... electrically optimistic!",
}

# Record the conversation
conversation_history = []

# Use input to get a response
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm not sure how to respond to that. Try asking something else or type 'help'."

# Save the conversation to a file
def save_conversation(history, filename="chat_log.txt"):
    with open(filename, "w") as file:
        file.write("=== ChatBot Conversation Log ===\n")
        for entry in history:
            file.write(entry + "\n")
    print(f"Conversation saved to '{filename}'.")

# Primary chatbot loop
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


# Launch the chatbot
if __name__ == "__main__":
    run_chatbot()
