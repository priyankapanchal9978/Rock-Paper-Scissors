from flask import Flask, render_template, request
import random

app = Flask(__name__)

user_score = 0
computer_score = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global user_score, computer_score

    user_choice = None
    computer_choice = None
    result = None

    if request.method == "POST":
        if "reset" in request.form:
            user_score = 0
            computer_score = 0
        else:
            user_choice = request.form["choice"]
            computer_choice = random.choice(["rock", "paper", "scissors"])

            if user_choice == computer_choice:
                result = "It's a Tie 🤝"
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "scissors" and computer_choice == "paper") or \
                 (user_choice == "paper" and computer_choice == "rock"):
                result = "You Win 🏆🔥"
                user_score += 1
            else:
                result = "You Lose 😢"
                computer_score += 1

    return render_template(
        "index.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        result=result,
        user_score=user_score,
        computer_score=computer_score
    )

if __name__ == "__main__":
    app.run(debug=True)     