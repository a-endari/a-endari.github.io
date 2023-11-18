from flask import Flask

app = Flask("__main__")


@app.route("/")
def index():
    return "<h1>Hello World!  I love you.</h1>"


@app.route("/new")
def new_page():
    return "hell no World"


if __name__ == "__main__":
    app.run(debug=True)
