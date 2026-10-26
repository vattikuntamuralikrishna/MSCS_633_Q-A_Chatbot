"""
Terminal Client Chatbot using Django, Python, and ChatterBot.
Author: [Your Name]
Description: Interactive terminal client that trains a ChatterBot instance 
             and processes user conversation lines in real-time.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def initialize_chatbot():
    """Initializes and configures the ChatterBot engine."""
    chatbot = ChatBot(
        'DjangoTerminalBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///db.sqlite3',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am not sure how to respond to that.',
                'maximum_similarity_threshold': 0.90
            },
            'chatterbot.logic.TimeLogicAdapter'
        ]
    )
    return chatbot

def train_chatbot(chatbot):
    """Trains the chatbot using the specific conversation dataset required."""
    trainer = ListTrainer(chatbot)
    
    # Training data matching the requested input/output interaction flow
    conversation = [
        "Good morning! How are you doing?",
        "I am doing very well, thank you for asking.",
        "You're welcome.",
        "Do you like hats?"
    ]
    
    trainer.train(conversation)
    print("[INFO] Bot training completed successfully.")

def run_terminal_client():
    """Runs the continuous interactive chat loop in the terminal."""
    chatbot = initialize_chatbot()
    train_chatbot(chatbot)
    
    print("\n" + "=" * 55)
    print(" Terminal Chatbot Active (Django / ChatterBot Backend)")
    print(" Type your message below. Type 'exit' or 'quit' to quit.")
    print("=" * 55 + "\n")

    while True:
        try:
            # Capture user input from the terminal
            user_input = input("user: ")
            
            # Check for termination commands
            if user_input.strip().lower() in ['exit', 'quit', ':q']:
                print("bot: Goodbye! Have a great day.")
                break
            
            # Skip empty inputs
            if not user_input.strip():
                continue
                
            # Generate and print bot response
            bot_response = chatbot.get_response(user_input)
            print(f"bot: {bot_response}")
            
        except (KeyboardInterrupt, EOFError, SystemExit):
            print("\nbot: Session terminated. Goodbye!")
            break

if __name__ == "__main__":
    run_terminal_client()