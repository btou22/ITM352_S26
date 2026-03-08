# Quiz game - full assignment version
# Name: Brandon Tou
# Date: Mar. 6, 2026

import json
import random
from string import ascii_uppercase


def load_questions(filename):
    with open(filename, "r") as file:
        return json.load(file)


def prepare_questions(raw_questions):
    question_list = []

    for question_text, options in raw_questions.items():
        correct_answer = options[0]
        shuffled_options = options[:]
        random.shuffle(shuffled_options)

        question_data = {
            "question": question_text,
            "options": shuffled_options,
            "correct_answer": correct_answer
        }
        question_list.append(question_data)

    random.shuffle(question_list)
    return question_list


def show_question(question_data, question_number, total_questions):
    print("\n" + "=" * 50)
    print(f"Question {question_number} of {total_questions}")
    print(question_data["question"])
    print("-" * 50)

    labels = {}
    for i, option in enumerate(question_data["options"]):
        label = ascii_uppercase[i]
        labels[label] = option
        print(f"{label}. {option}")

    return labels


def get_valid_choice(valid_labels):
    while True:
        choice = input("Choice? ").strip().upper()
        if choice in valid_labels:
            return choice
        print("Invalid choice. Please enter one of:", ", ".join(valid_labels))


def ask_question(question_data, question_number, total_questions):
    labels = show_question(question_data, question_number, total_questions)

    while True:
        user_choice = get_valid_choice(labels.keys())
        chosen_answer = labels[user_choice]

        if chosen_answer == question_data["correct_answer"]:
            print("Correct!")
            return 1
        else:
            print("Wrong. Try again.")


def run_quiz(questions):
    num_correct = 0
    total_questions = len(questions)

    for i, question_data in enumerate(questions, start=1):
        num_correct += ask_question(question_data, i, total_questions)

    print("\n" + "=" * 50)
    print(f"You got {num_correct} out of {total_questions} correct.")
    print("=" * 50)


def main():
    filename = "questions.json"

    try:
        raw_questions = load_questions(filename)
        questions = prepare_questions(raw_questions)
        run_quiz(questions)
    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
    except json.JSONDecodeError:
        print(f"Error: {filename} is not valid JSON.")


if __name__ == "__main__":
    main()