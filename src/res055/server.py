from random import randint

from flask import Flask

app = Flask(__name__)


def h1(func):
    def wrapper():
        return f"<h1>{func()}</h1>"

    return wrapper


def happy_cat(func):
    def wrapper():
        return (
            f'<p>{func()}</p><iframe src="https://giphy.com/embed/K1tgb1IUeBOgw"'
            ' width="480" height="278" frameBorder="0" class="giphy-embed"'
            " allowFullScreen></iframe><p><a"
            ' href="https://giphy.com/gifs/kitten-meow-K1tgb1IUeBOgw">via'
            " GIPHY</a></p>"
        )

    return wrapper


def sad_cat(func):
    def wrapper(*args):
        return (
            f"<p>{func(args[0])}</p>"
            '<iframe src="https://giphy.com/embed/CM1rHbKDMH2BW" width="480"'
            ' height="360" frameBorder="0" class="giphy-embed"'
            " allowFullScreen></iframe><p><a"
            ' href="https://giphy.com/gifs/sad-kitten-CM1rHbKDMH2BW">via GIPHY</a></p>'
        )

    return wrapper


@app.route("/")
@h1
def frontpage():
    return "Guess a number between 0 and 9."


@sad_cat
def higher(number):
    return f"{number} is too high, try again."


@sad_cat
def lower(number):
    return f"{number} is too low, try again."


@happy_cat
def correct():
    return "That's correct!"


@app.route("/<int:number>")
def test(number):
    if number < answer:
        return lower(number)
    elif number > answer:
        return higher(number)
    else:
        return correct()


if __name__ == "__main__":
    answer = randint(0, 9)
    app.run(debug=True)
