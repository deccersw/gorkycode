from flask import Flask, render_template, redirect, url_for
from event import CreateEvent
import psycopg2

conn = psycopg2.connect(database='gorkycode',
            user='postgres',
            password='postgres',
            host='127.0.0.1',
            port=5432) # подключились к базе данных

# id_number = 1 # id мероприятия в базе данных

# cur = conn.cursor()

# cur.execute("select * from information_schema.tables where table_name=%s", ('events',))
# if bool(cur.rowcount) == False:
#         id_number = 1
#         cur.execute(
#             """
#                 CREATE TABLE events
#                 (
#                     id INTEGER,
#                     sport CHARACTER VARYING(2000),
#                     event_type CHARACTER VARYING(2000),
#                     count_people INTEGER,
#                     date CHARACTER VARYING(2000),
#                     time CHARACTER VARYING(2000),
#                     place CHARACTER VARYING(2000)
#                 )
#             """
#         )

# else:
#     cur.execute(
#         """
#             SELECT * FROM events
#         """
#     )
#     events = cur.fetchall()[-1]
#     id_number = events[0] + 1

# conn.commit()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random string'


@app.route("/")
def base():
    return render_template("main_page.html")


@app.route("/create", methods=['GET', 'POST'])
def create():
    # global id_number
    form = CreateEvent()
    # print(form.kind_of_sport.data)
    # print(form.district.data)
    # print(form.place.data)
    # print(form.place.data)
    # print(form.date.data)
    # print(form.time.data)
    # print(form.description.data)

    if form.validate_on_submit():
        cur = conn.cursor()
        # form.count_of_people.data - тоже вернуть     "count_people": []
        # INSERT INTO events (kind_sport, type_event, count_people, district, place, date, time, description) - ВЕРНУТЬ ОБРАТНО
        cur.execute(
            """
                INSERT INTO events (kind_sport, type_event, count_people, district, place, date, time, description)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (form.kind_of_sport.data, form.type_of_event.data, form.count_of_people.data, form.district.data, form.place.data, form.date.data, form.time.data, form.description.data)
        )
        conn.commit()
        # cur.close()
        # id_number += 1

        return redirect("/")

    return render_template('index.html', form=form)

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
    
    dict_of_params = {"kindSport": [], "typeEvent": [], "count_people": [], "district": [], "place": [], "date": [], "time": [], "description": []}
    for event in events:
        index = 1
        for param in dict_of_params.keys():
            dict_of_params[param].append(event[index])
            index += 1
    
    return render_template("view.html", dict=dict_of_params, len=events_len)


if __name__ == "__main__":
    app.run()
