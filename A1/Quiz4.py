# Quiz game.  Fourth version.
# Name: Brandon Tou
# Date: Feb. 28, 2026
# Make a list with the questions and correct answers.
# Make QUESTIONS a dictionary, to include answer options and the correct choice.
# Allow the user to select the correct answer by a label.

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "Houston", "Dallas", "San Antonio"],
    "The Last Supper was painted by which artist?": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
    }

for question, options in QUESTIONS.items():
    correct_answer = options[0]  # The first option is the correct answer
    sorted_options = sorted(options)
    for label, alternative in enumerate(sorted_options, start=1):
        print(f" {label}. {alternative}")

    answer_label = int(input(question + ": "))
    answer = sorted_options[answer_label - 1]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is '{correct_answer}' not {answer!r}")