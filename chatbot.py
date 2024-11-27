import nltk
from nltk.chat.util import Chat, reflections


nltk.download('punkt')


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello! How can I assist you?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you.",]
    ],
    [
        r"how are you?",
        ["I'm just a program, but thanks for asking!",]
    ],
    [
        r"sorry (.*)",
        ["No problem!",]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a nice day!",]
    ],
    [
        r"(.*) your (.*) favorite color?",
        ["I don't have preferences, but what's yours?",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Can you ask something else?",]
    ],
]
chatbot = Chat(pairs, reflections)

def chatbot_conversation():
    print("Welcome to the Python Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print(f"Chatbot: {response}")

chatbot_conversation()
