import tkinter as tk
import random

questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the square root of 64?": "8",
    "What is the chemical symbol for water?": "H2O",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the smallest prime number?": "2",
    "In which continent is Egypt located?": "Africa",
    "What is the capital of Japan?": "Tokyo",
    "What gas do plants absorb from the atmosphere?": "Carbon dioxide",
    "How many legs does a spider have?": "8",
    "What is the boiling point of water in Celsius?": "100",
    "Who is known as the father of computers?": "Charles Babbage",
    "What planet is known as the Red Planet?": "Mars",
    "Which ocean is the largest?": "Pacific Ocean",
    "What is the hardest natural substance on Earth?": "Diamond",
    "How many continents are there?": "7",
    "Who discovered gravity?": "Isaac Newton",
    "What is the tallest mountain in the world?": "Mount Everest",
    "What is the capital of Australia?": "Canberra",
    "Which organ pumps blood through the body?": "Heart",
    "What is the main language spoken in Brazil?": "Portuguese",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "Which planet has rings around it?": "Saturn",
    "What is the currency of the United Kingdom?": "Pound sterling",
    "How many degrees are in a circle?": "360",
    "What is the largest mammal in the world?": "Blue whale",
    "Who was the first man to walk on the moon?": "Neil Armstrong",
    "Which country is known as the Land of the Rising Sun?": "Japan",
    "What do bees make?": "Honey",
    "What is the primary color of a ripe banana?": "Yellow",
    "Which country gifted the Statue of Liberty to the USA?": "France",
    "How many bones are there in the adult human body?": "206",
    "What instrument measures temperature?": "Thermometer",
    "What is the capital of Canada?": "Ottawa",
    "What is the process of water turning into vapor called?": "Evaporation",
    "Which animal is known as the king of the jungle?": "Lion",
    "How many days are there in a leap year?": "366",
    "Which planet is closest to the sun?": "Mercury",
    "What is the largest internal organ in the human body?": "Liver",
    "Who invented the telephone?": "Alexander Graham Bell",
    "What is the national sport of Japan?": "Sumo wrestling",
    "What is the fastest land animal?": "Cheetah",
    "What is the study of the stars and planets called?": "Astronomy",
    "Which insect is known for its beautiful wings?": "Butterfly",
    "Which country is the Eiffel Tower located in?": "France",
    "Which color is made by mixing red and white?": "Pink",
    "Which bird is a symbol of peace?": "Dove",
    "What is the freezing point of water in Celsius?": "0",
    "What is the capital of Italy?": "Rome",
    "What is the name of the fairy in Peter Pan?": "Tinker Bell",
    "What natural satellite orbits the Earth?": "The Moon",
    "Which country has the most population?": "China"
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
