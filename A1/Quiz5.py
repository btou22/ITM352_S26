# Quiz game.  Fifth version.
# Name: Brandon Tou
# Date: Feb. 28, 2026
# Make a list with the questions and correct answers.
# Make QUESTIONS a dictionary, to include answer options and the correct choice.
# Allow the user to select the correct answer by a label.
# Improve look and usability. Keep track of correct answers.

from string import ascii_lowercase

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "Houston", "Dallas", "San Antonio"],
    "The Last Supper was painted by which artist?": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"],
    "What is the capital of France?" : ["Paris", "London", "Rome", "Berlin"],
    "Which planet is known as the Red Planet?": ["Mars", "Venus", "Jupiter", "Saturn"]
}

num_correct = 0
for num, (question, options) in enumerate(QUESTIONS.items(), start=1):
    print(f"Question {num}:")
    print(question)
    correct_answer = options[0]  # The first option is the correct answer
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(options)))
    for label, alternative in labeled_alternatives.items():
        print(f" {label}. {alternative}")
    
    answer_label = input("Choice? ")
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    else:
        print(f"The answer is '{correct_answer}' not {answer!r}")

print(f"You got {num_correct} out of {len(QUESTIONS)} correct.")