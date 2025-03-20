import tkinter as tk
import random

questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the square root of 64?": "8"
}

current_question = ""

def new_question():
    global current_question
    current_question = random.choice(list(questions.keys()))
    question_label.config(text=current_question)
    entry.delete(0, tk.END)


def check_answer():
    user_answer = entry.get().strip()
    if user_answer.lower() == questions[current_question].lower():
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text=f"Wrong! Answer: {questions[current_question]}", fg="red")
    root.after(2000, new_question)

root = tk.Tk()
root.title("Flashcard Quiz App")
root.geometry("400x300")

question_label = tk.Label(root, text="Click 'Next' for a question", font=("Arial", 14), wraplength=350)
question_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

check_button = tk.Button(root, text="Check Answer", command=check_answer)
check_button.pack(pady=5)

next_button = tk.Button(root, text="Next Question", command=new_question)
next_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

new_question()
root.mainloop()
