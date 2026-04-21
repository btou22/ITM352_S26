from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = "secret"  # Secret key for sessions

# Load questions from the quiz.json file
with open("quiz.json", "r") as f:
    questions = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')  # Start page

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Initialize session if it's the first time accessing quiz
    if "index" not in session:
        session["index"] = 0
        session["score"] = 0

    # Check if the quiz has finished
    if session["index"] >= len(questions):
        return redirect(url_for("result"))

    # Handle POST request when user submits answer
    if request.method == "POST":
        user_answer = request.form.get("answer")  # Use get in case it's missing
        if user_answer:
            current_q = questions[session["index"]]  # Current question

            # Check if the user's answer is correct
            if user_answer == current_q["answer"]:
                session["score"] += 1  # Increment score if correct

        # Move to the next question
        session["index"] += 1

        # If there are no more questions, redirect to the result page
        if session["index"] >= len(questions):
            return redirect(url_for("result"))

    # Show the current question
    q = questions[session["index"]]
    return render_template("quiz.html", question=q)

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