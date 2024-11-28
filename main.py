from flask import Flask, render_template, redirect, url_for
from event import CreateEvent
import psycopg2

conn = psycopg2.connect(database='gorkycode',
            user='postgres',
            password='postgres',
            host='127.0.0.1',
            port=5432) # подключились к базе данных

id_number = 1 # id мероприятия в базе данных

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random string'


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateEvent()
    if form.validate_on_submit():
        cur = conn.cursor()
        cur.execute(
            """
                INSERT INTO events (id, sport, event_type, count_people, date, time, place)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (id_number, form.kind_of_sport.data, form.type_of_event.data, form.count_of_people.data, form.date.data, form.time.data, form.place.data)
        )
        conn.commit()
        # cur.close()
        id_number += 1

        return redirect("/")

    return render_template('create.html', form=form)


if __name__ == "__main__":
    app.run()
