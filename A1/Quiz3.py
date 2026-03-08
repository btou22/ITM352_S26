# Quiz game.  Third version.
# Name: Brandon Tou
# Date: Feb. 28, 2026
# Make a list with the questions and correct answers.
# Make QUESTIONS a dictionary, to include answer options and the correct choice.

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "Houston", "Dallas", "San Antonio"],
    "The Last Supper was painted by which artist?": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
    }

for question, options in QUESTIONS.items():
    correct_answer = options[0]  # The first option is the correct answer
    for alternative in sorted(options):
        print(f" - {alternative}")

    answer = input(question + ": ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is '{correct_answer}' not {answer!r}")
    