import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Thanks for visiting!"
    current_year = datetime.datetime.now().year
    return render_template("index.html", some_text=some_text, current_year=current_year)


@app.route("/about")
def about_me():
    some_text = "Thanks for visiting!"
    current_year = datetime.datetime.now().year
    return render_template("about.html", some_text=some_text, current_year=current_year)


@app.route("/portfolio")
def portfolio():
    some_text = "Thanks for visiting!"
    current_year = datetime.datetime.now().year
    return render_template("portfolio.html", some_text=some_text, current_year=current_year)


@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("/portfolio/fakebook.html")


@app.route("/portfolio/boogle")
def boogle():
    return render_template("/portfolio/boogle.html")


@app.route("/portfolio/hair-salon")
def hairsalon():
    return render_template("/portfolio/hair-salon.html")


if __name__ == '__main__':
    app.run()
