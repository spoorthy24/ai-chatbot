from nltk.chat.util import Chat, reflections
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import datetime
# Simple rule-based chatbot using NLTK
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what are you doing?",
        ["waiting to assist you :)"]
    ],
    [
        r"sup|whatsup?",
        ["Nothing much Sup with you?"]
    ],
    [
        r"what is your name ?",
        ["I am ChatBot,What is your name?"]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?"]
    ],
    [
        r"what is the time?|time|whats the time?",
        [f"The current time is {datetime.datetime.now().strftime('%H:%M')}"]
    ],
    [
        r"what is today's date?|today's date|date",
        [f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry"]
    ],
    [
        r"pick me number from 1 to 10",
        ["1","2","3","4","5","6","7","8","9","10"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye, take care!", "Nice chatting with you. Goodbye!"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "I'm afraid for the calendar. Its days are numbered.",
         "Dear Math, grow up and solve your own problems.", "I only know 25 letters of the alphabet. I don't know y."]
    ],
    [
        r"that was funny|lol|haha",
        ["glad you liked it :)"]
    ],

    [
        r"what is the time?",
        ["I'm sorry, I am not programmed to provide real-time information."]
    ],
    [
        r"what is your favorite color?",
        ["I don't have a favorite color. I'm a chatbot!"]
    ],
    [
        r"what is the meaning of life?",
        ["The meaning of life is a philosophical question that has different interpretations for different people."]
    ],
    [
        r"where are you from?",
        ["I am an AI chatbot programmed by OpenAI. I don't have a physical location."]
    ],
    [
        r"how old are you?",
        ["As an AI chatbot, I don't have an age. I'm always learning and improving!"]
    ],
    [
        r"what do you like to do?",
        ["I enjoy having conversations and helping users with their questions."]
    ],
    [
        r"what is your purpose?",
        ["My purpose is to assist users, provide information, and engage in conversations."]
    ],
    [
        r"what is the weather like today?",
        ["I'm sorry, I don't have access to real-time weather information."]
    ],
    [
        r"can you recommend a movie?",
        ["Sure! What genre or type of movie are you interested in?"]
    ],
    [
        r"what is your favorite book?",
        ["As a chatbot, I don't read books. But I can recommend popular ones if you'd like!"]
    ],
    [
        r"tell me something fascinating",
        ["Did you know that the world's oldest known living organism is a tree called Methuselah, which is over 4,800 years old?"]
    ],
    [
        r"what is the capital of (.*)",
        ["The capital of %1 is..."]
    ],
]

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}

chatbot = ChatBot('MyChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)

# Create an NLTK chatbot
def nltk_chatbot():
    print("NLTK ChatBot: Hello, How can I assist you today?")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("User: ")
        if user_input.lower() == "bye":
            print("NLTK ChatBot: Goodbye!")
            break
        else:
            print("NLTK ChatBot:", chat.respond(user_input))

# Create a ChatterBot chatbot
def chatterbot():
    print("ChatterBot: Hello, How can I assist you today?")
    chatbot = ChatBot('MyChatBot')
    trainer.train("chatterbot.corpus.english")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "bye":
            print("ChatterBot: Goodbye!")
            break
        else:
            response = chatbot.get_response(user_input)
            print("ChatterBot:", response)

# Main program
print("Select Chatbot:")
print("1. NLTK ChatBot")
print("2. ChatterBot")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    nltk_chatbot()
elif choice == "2":
    chatterbot()
else:
    print("Invalid choice. Exiting...")
