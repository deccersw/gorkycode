from flask import Flask, render_template, redirect, url_for
from event import CreateEvent
import psycopg2

conn = psycopg2.connect(database='gorkycode',
            user='postgres',
            password='postgres',
            host='127.0.0.1',
            port=5432) # подключились к базе данных

id_number = 0 # id мероприятия в базе данных

cur = conn.cursor()

cur.execute("select * from information_schema.tables where table_name=%s", ('events',))
if bool(cur.rowcount) == False:
        id_number = 1
        cur.execute(
            """
                CREATE TABLE events
                (
                    id INTEGER,
                    sport CHARACTER VARYING(2000),
                    event_type CHARACTER VARYING(2000),
                    count_people INTEGER,
                    date CHARACTER VARYING(2000),
                    time CHARACTER VARYING(2000),
                    place CHARACTER VARYING(2000)
                )
            """
        )

else:
    cur.execute(
        """
            SELECT * FROM events
        """
    )
    events = cur.fetchall()[-1]
    id_number = events[0] + 1

conn.commit()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random string'


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/create", methods=['GET', 'POST'])
def create():
    global id_number
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

@app.route("/created_events")
def created_events():
    cur = conn.cursor()
    cur.execute(
        """
            SELECT * FROM events
        """
    )
    events = cur.fetchall()

    events_len = len(events)
    # print(len(events))
    
    dict_of_params = {"kindSport": [], "typeEvent": [], "count_people": [], "time": [], "date": [], "place": []}
    for event in events:
        index = 1
        for param in dict_of_params.keys():
            dict_of_params[param].append(event[index])
            index += 1
    
    return render_template("created_events.html", dict=dict_of_params, len=events_len)


if __name__ == "__main__":
    app.run()
