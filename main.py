from flask import Flask, render_template, redirect, url_for
from event import CreateEvent
from psycopg2 import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random string'


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateEvent()
    if form.validate_on_submit():
        print(134)
        # con = connect("")
        return render_template('base.html')
    # print(form.kind_of_sport)
    # print(form.kind_of_sport.data)
    return render_template('create.html', form=form)


if __name__ == "__main__":
    app.run()
