import tkinter as tk
from tkinter import scrolledtext

responses = {
    "hi": "Hello! I am HealthBot. How can I assist you today?",
    "hello": "Hi! Do you have a health-related question?",
    "i have a headache": "You should rest, stay hydrated, and take a mild pain reliever if needed.",
    "what should i do if i have a fever?": "Drink plenty of fluids and rest. If the fever persists, please consult a doctor.",
    "i feel dizzy": "Sit down, breathe deeply, and drink water. If it continues, seek medical help.",
    "what should i eat for a cold?": "Warm fluids, soups, citrus fruits, and light meals help during a cold.",
    "how to stay healthy?": "Eat balanced meals, exercise regularly, stay hydrated, and get enough sleep.",
    "what should i do in case of a cut?": "Clean the wound with water, apply antiseptic, and cover it with a clean bandage.",
    "how much water should i drink daily?": "Generally, 2 to 3 liters per day is recommended, but it varies based on your activity.",
    "thank you": "You’re welcome! Take care.",
    "bye": "Goodbye! Stay healthy."
}

root = tk.Tk()
root.title("HealthBot")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_area.pack(padx=10, pady=10)
chat_area.config(state='disabled')

user_input = tk.Entry(root, width=40, font=("Arial", 12))
user_input.pack(padx=10, pady=5, side=tk.LEFT)

def send_message():
    message = user_input.get().strip().lower()
    if message:
        chat_area.config(state='normal')
        chat_area.insert(tk.END, "You: " + message + "\n")
        
        reply = responses.get(message, "I'm sorry, I can assist with basic health tips. Please ask another question.")
        chat_area.insert(tk.END, "HealthBot: " + reply + "\n\n")
        
        chat_area.config(state='disabled')
        chat_area.yview(tk.END)
        
        user_input.delete(0, tk.END)
        
        if message == "bye":
            root.after(2000, root.destroy)

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(padx=10, pady=5, side=tk.LEFT)

chat_area.config(state='normal')
chat_area.insert(tk.END, "HealthBot: Hello! I am HealthBot. How can I assist you today?\n\n")
chat_area.config(state='disabled')

root.bind('<Return>', lambda event: send_message())

root.mainloop()
