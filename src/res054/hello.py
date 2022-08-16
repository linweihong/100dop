from flask import Flask

app = Flask(__name__)


def strong(func):
    def wrapper():
        return f"<strong>{func()}</strong>"

    return wrapper

def em(func):
    def wrapper():
        return f"<em>{func()}</em>"

    return wrapper


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def bye():
    return "Bye."


@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}."


if __name__ == "__main__":
    app.run(debug=True)
