from flask import Flask, render_template, request, redirect, url_for, session
from string import ascii_lowercase
import south_park_questions as sp  # your questions file

app = Flask(__name__)
app.secret_key = "your_secret_key"  # required for session tracking

# Only one quiz for now
QUIZZES = {
    "south_park": sp.QUESTIONS
}


@app.route("/")
def index():
    """Home page: choose quiz"""
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start():
    """Initialize quiz session"""
    selected_quiz = request.form.get("quiz")  # e.g., "south_park"

    # Convert dictionary items to a list of tuples
    session["quiz"] = list(QUIZZES[selected_quiz].items())
    session["current_q"] = 0
    session["score"] = 0
    session["show_explanation"] = False
    session["last_explanation"] = ""

    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """Display questions and handle answers"""
    quiz_data = session.get("quiz", [])
    current_q = session.get("current_q", 0)

    # If finished, go to result
    if current_q >= len(quiz_data):
        return redirect(url_for("result"))

    # Unpack question
    question_text, (choices, explanation) = quiz_data[current_q]

    # Label choices a, b, c, d
    answer_choices = dict(zip(ascii_lowercase, sorted(choices)))

    if request.method == "POST":
        selected = request.form.get("answer")
        if selected in answer_choices:
            chosen_answer = answer_choices[selected]

            # Correct answer is always the first in the original list
            if chosen_answer == choices[0]:
                session["score"] += 1

            # Save explanation to show
            session["last_explanation"] = explanation
            session["show_explanation"] = True

        # Move to next question on next GET
        session["current_q"] += 1
        return redirect(url_for("quiz"))

    # If coming from POST, show explanation first
    show_explanation = session.get("show_explanation", False)
    last_explanation = session.get("last_explanation", "")

    # Reset explanation flag
    session["show_explanation"] = False
    session["last_explanation"] = ""

    return render_template(
        "quiz.html",
        question=question_text,
        choices=answer_choices,
        q_number=current_q + 1,
        show_explanation=show_explanation,
        explanation=last_explanation
    )


@app.route("/result")
def result():
    """Show final results"""
    score = session.get("score", 0)
    total = len(session.get("quiz", []))

    # Save quiz history
    with open("quiz_history.txt", "a") as f:
        f.write(f"South Park Quiz: {score} out of {total}\n")

    return render_template("result.html", score=score, total=total)


@app.route("/restart")
def restart():
    """Restart quiz from beginning"""
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)