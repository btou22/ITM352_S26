# Quiz game.  Second version.
# Name: Brandon  Tou
# Date: Feb. 28, 2026
# Make a list with the questions and correct answers.

QUESTIONS = [
    ("What is the airspeed of an unladen swallow in miles/hr?", "12"),
    ("What is the capital of Texas?", "Austin"),
    ("The Last Supper was painted by which artist?", "Da Vinci")
]

for question, correct_answer in QUESTIONS:
    answer = input(question + ": ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is '{correct_answer}' not {answer!r}")