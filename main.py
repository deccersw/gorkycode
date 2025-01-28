from flask import Flask, render_template, redirect
from event import CreateEvent
import sqlite3

conn = sqlite3.connect("basa.db")

cur = conn.cursor()

try:
    cur.execute("""SELECT * from events""").fetchall()
except Exception as ex:
    cur.execute(
        """
            CREATE TABLE events
            (
                id SERIAL PRIMARY KEY,
                kind_sport CHARACTER VARYING(2000),
                type_event CHARACTER VARYING(2000),
                count_people INTEGER,
                district CHARACTER VARYING(2000),
                place CHARACTER VARYING(2000),
                date CHARACTER VARYING(2000),
                time CHARACTER VARYING(2000),
                description CHARACTER VARYING(5000)
            )
        """
    )
    print(ex)


conn.commit()
conn.close()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random string'


@app.route("/")
def base():
    return render_template("main_page.html")


@app.route("/create", methods=['GET', 'POST'])
def create():
    global id_number
    form = CreateEvent()

    if form.validate_on_submit():
        conn = sqlite3.connect("basa.db")
        cur = conn.cursor()
        # form.count_of_people.data - тоже вернуть     "count_people": []
        # INSERT INTO events (kind_sport, type_event, count_people, district, place, date, time, description) - ВЕРНУТЬ ОБРАТНО
        cur.execute(
            """
                INSERT INTO events (kind_sport, type_event, count_people, district, place, date, time, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (form.kind_of_sport.data, form.type_of_event.data, form.count_of_people.data, form.district.data,
             form.place.data, form.date.data, form.time.data, form.description.data)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template('index.html', form=form)

@app.route("/created_events")
def created_events():
    conn = sqlite3.connect("basa.db")
    cur = conn.cursor()
    cur.execute(
        """
            SELECT * FROM events
        """
    )
    events = cur.fetchall()

    events_len = len(events)
    # print(len(events))
    
    dict_of_params = {"kindSport": [], "typeEvent": [], "count_people": [], "district": [], "place": [], "date": [],
                      "time": [], "description": []}
    for event in events:
        index = 1
        for param in dict_of_params.keys():
            dict_of_params[param].append(event[index])
            index += 1
    
    return render_template("view.html", dict=dict_of_params, len=events_len)


if __name__ == "__main__":
    app.run()
