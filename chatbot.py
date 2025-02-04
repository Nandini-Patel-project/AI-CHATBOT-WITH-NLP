import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

# Ensure NLTK data is downloaded
nltk.download('punkt')

# Define patterns and responses
pairs = [
    (r'Hi|Hello', ['Hello! How can I help you today?']),
    (r'What is your name|name please|your name', ['I am a chatbot created with NLTK.']),
    (r'How are you?', ['I am just a program, but I am doing great!']),
    (r'What can you do?', ['I can answer questions and help you with various tasks.']),
    (r'When were you developed?', ['I was created using NLTK. I am constantly improving!']),
    (r'(.*) your (.*)', ['Why are you asking about my %2?']),
    (r'(.*)', ['I am not sure how to respond to that. Can you ask something else?']),
    (r'quit|Bye', ['Goodbye! Have a nice day!']),
]

# Define chatbot function
def chatbot_response(user_input):
    chat = Chat(pairs, reflections)
    response = chat.respond(user_input)
    if response:
        return response
    else:
        return "I am not sure how to respond to that."

# Create the GUI window
def create_gui():
    window = tk.Tk()
    window.title("Chatbot")
    
    # Create a scrollable text box for displaying conversation
    conversation_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
    conversation_area.grid(row=0, column=0, padx=10, pady=10)
    conversation_area.config(state=tk.DISABLED)

    # Function to handle user input and update the conversation area
    def send_message():
        user_message = user_input.get()
        if user_message.lower() == 'quit':
            conversation_area.config(state=tk.NORMAL)
            conversation_area.insert(tk.END, "You: " + user_message + "\n")
            conversation_area.insert(tk.END, "Chatbot: Goodbye! Have a nice day!\n")
            conversation_area.config(state=tk.DISABLED)
            window.quit()  # Close the application
        else:
            conversation_area.config(state=tk.NORMAL)
            conversation_area.insert(tk.END, "You: " + user_message + "\n")
            response = chatbot_response(user_message)
            conversation_area.insert(tk.END, "Chatbot: " + response + "\n")
            conversation_area.config(state=tk.DISABLED)
            user_input.delete(0, tk.END)

    # Create input field for the user
    user_input = tk.Entry(window, width=50, font=("Arial", 12))
    user_input.grid(row=1, column=0, padx=10, pady=10)

    # Create send button
    send_button = tk.Button(window, text="Send", width=15, height=2, command=send_message, font=("Arial", 12))
    send_button.grid(row=2, column=0, pady=10)

    window.mainloop()

# Run the GUI chatbot
if __name__ == "__main__":
    create_gui()


# run by :  & C:/Users/user/AppData/Local/Programs/Python/Python313/python.exe c:/Users/user/Desktop/task_3/chatbot.py