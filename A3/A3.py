from flask import Flask, render_template, request, redirect, url_for, session
import json
import random

# session is used to temporarily keep track of a user's progress
# random is used to shuffle the questions

app = Flask(__name__)
app.secret_key = "secret"

with open("adventure_time.json", "r") as f:
    questions = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if "index" not in session or "question_order" not in session:
        # this code initializes a session for the user if it's their first time accessing.
        session["index"] = 0
        # index is the question number.
        session["score"] = 0
        # score is the correct answers user answers.
        session["question_order"] = list(range(len(questions)))
        random.shuffle(session["question_order"])
        # this code was created by AI, using the prompt
        # "How would I use random in order to shuffle the questions for the user?"

    if session["index"] >= len(questions):
        return redirect(url_for("result"))
        # this code will end and redirect to result if index is equal to length of questions

    if request.method == "POST":  # user submits an answer from the page
        if "next" in request.form:
            session["index"] += 1

            session.pop("explanation", None)
            session.pop("result", None)

            if session["index"] >= len(questions):
                return redirect(url_for("result"))

        else:
            # compares user's answer to correct answer from the list.
            user_answer = request.form.get("answer")

            if user_answer:
                q_index = session["question_order"][session["index"]]
                current_q = questions[q_index]

                # if the user submits an answer, it will retrieve the question from the
                # questions list by its index.
                if user_answer == current_q["answer"]:
                    session["score"] += 1
                    # if the answer matches the current question, the session adds 1 to the score.
                    session["result"] = "Correct!"
                else:
                    session["result"] = "Wrong."

                # this code provides an explanation for the answer despite whether the answer is correct.
                session["explanation"] = current_q["explanation"]

    q_index = session["question_order"][session["index"]]
    q = questions[q_index]

    choices = q["choices"][:]
    random.shuffle(choices)
    # this code was created by AI, using the prompt
    # "How would I use random to shuffle the choices for each question?"

    return render_template(
        "quiz.html",
        question=q,
        choices=choices,
        explanation=session.get("explanation"),
        result=session.get("result"),
        current_question=session["index"] + 1,
        total_questions=len(questions)
    )

@app.route("/result")
def result():
    # Get score from session and render result page
    score = session.get("score", 0)
    session.clear()  # Clear session after showing result
    return render_template("result.html", score=score, total=len(questions))

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()