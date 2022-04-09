from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0,9)

@app.route("/")
def guess():
    return "<h1>Guess a number between 0 and 9</h1>"

@app.route("/<int:number>")
def input_number(number):
    if number > random_number:
        return f'<h1 style="color: purple">Too high, try again!</h1>'
    elif number < random_number:
        return f'<h1 style="color: red">Too low, try again</h1>'
    else:
        return f'<h1 style="color: green">You found me!</h1>'
    

if __name__ == "__main__":
    app.run(debug=True)