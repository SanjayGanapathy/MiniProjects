import tkinter as tk
from tkinter import scrolledtext
import random
import re

class TherabotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Therabot - Your Personal Therapy Bot")
        self.root.geometry("500x400")
        self.root.configure(bg="#e6f2ff")  # Light blue background color

        self.header_label = tk.Label(root, text="Therabot - Your Personal Therapy Bot", font=("Helvetica", 16), bg="#e6f2ff")
        self.header_label.pack(pady=10)

        self.chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Helvetica", 12), bg="white")
        self.chat_history.pack(pady=10)

        self.input_label = tk.Label(root, text="You:", font=("Helvetica", 12), bg="#e6f2ff")
        self.input_label.pack()

        self.user_input = tk.Entry(root, width=50, font=("Helvetica", 12))
        self.user_input.pack(pady=10)

        self.send_button = tk.Button(root, text="Send", command=self.send_message, font=("Helvetica", 12), bg="#66cc66", fg="white")
        self.send_button.pack()
         # Set the icon
        icon_path = ""  # Replace with the path to your icon file
        self.root.iconbitmap(icon_path)

        # Create a list of pre-defined responses with placeholders
        self.responses = {
            "greeting": ["Hey there! How's your day going? I'm here to chat and offer support."],
            "i feel (.*)": ["I'm here for you. Why do you feel {}?", "How has your mood been lately, feeling {}?"],
            "i am (.*)": ["That's interesting. Why do you say you're {}?", "How long have you been {}?"],
            "i'm (.*)": ["Why are you {}?", "How long have you been {}?"],
            "i (.*) myself": ["I'm really sorry to hear that. Why do you {} yourself?", "Can you share more about what makes you feel like {}ing yourself?"],
            "(.*) sorry (.*)": ["No need to apologize. Everyone makes mistakes. What are you sorry for?", "It's okay. What made you say sorry for {}?"],
            "(.*) friend (.*)": ["Friends are important. Tell me more about your friend.", "How do your friends make you feel?"],
            "yes": ["You seem positive! That's great. What's making you feel positive?", "Awesome! Can you share what's making you say yes?"],
            "no": ["Why not? I'm here to listen. What's on your mind?", "Okay. Let's talk about what's going on. Why do you say no?"],
            "mad": ["I'm sorry to hear that you're feeling mad. What happened?", "It's okay to feel mad sometimes. Can you tell me more about what's bothering you?"],
            "study": ["Not studying enough can be stressful. What's been challenging about your study routine?", "I understand. Balancing studies can be tough. What specifically didn't go well with your study session?"],
            "(.*)": ["Really? Please tell me more.", "Let's dive deeper into that. What else can you share?", "I'm here to listen. Can you elaborate on that?"]
        }

        # Initialize chat history
        self.chat_history.insert(tk.END, "Welcome to Therabot, your personal therapy bot\nRelease any emotions you might have charged up.\nTherabot does not judge you in any way, nor does it\nstore any information. Feel free to confess, or open up \nto Therabot!  Type 'Hey' to start, and 'Bye' to Exit.\n\n")

    def send_message(self):
        user_input = self.user_input.get().strip()
        self.chat_history.insert(tk.END, f"You: {user_input}\n")

        if re.search(r"\bbye\b", user_input, re.IGNORECASE):  # Check if "bye" is present in the input
            self.chat_history.insert(tk.END, "Therabot: Goodbye.\n")
            self.root.quit()
        else:
            response = self.match_response(user_input)
            self.chat_history.insert(tk.END, f"Therabot: {response}\n")
            self.user_input.delete(0, tk.END)

    def match_response(self, input_text):
        greeting_pattern = re.compile(r"^(hi(.*)|hello(.*)|hey(.*)|greetings(.*)|good (morning|afternoon|evening)(.*))$", re.IGNORECASE)
        if greeting_pattern.match(input_text):
            return random.choice(self.responses["greeting"])

        for pattern, response_list in self.responses.items():
            if pattern != "greeting":
                matches = re.search(pattern, input_text, re.IGNORECASE)
                if matches:
                    chosen_response = random.choice(response_list)
                    return chosen_response.format(*matches.groups()) if matches.groups() else chosen_response

        return "I'm sorry, I don't understand what you are saying. Please try saying something else."

# Create Tkinter GUI
root = tk.Tk()
app = TherabotGUI(root)

# Run Tkinter main loop
root.mainloop()
