from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, IntegerField, SelectField, TimeField
from wtforms.validators import DataRequired
from datetime import datetime


class CreateEvent(FlaskForm):
    kind_of_sport = SelectField('Выберите вид спорта', choices=[("бег", "Бег"), ('плавание', 'Плавание'),
                                                    ('настольный теннис', 'Настольный теннис'), ('шахматы', 'Шахматы'),
                                                    ('футбол', 'Футбол'), ('оздоровительный', 'Оздоровительный')],
                                validators=[DataRequired()])
    type_of_event =  SelectField('Тип мероприятия', choices=[("Соревнование", "Соревнование"), ('Тренировка', 'Тренировка'),
                                                    ('Любительская игра', 'Любительская игра'), ('Зарядка', 'Зарядка'),
                                                    ('Пробежка', 'Пробежка')],
                                validators=[DataRequired()])
    count_of_people = IntegerField('Количество участников', validators=[DataRequired()])
    time = TimeField('Время', validators=[DataRequired()])
    date = DateField('Дата', validators=[DataRequired()], default=datetime.today(), format='%Y-%m-%d')
    place = StringField('Место', validators=[DataRequired()])
    submit = SubmitField("Создать")

    def str(self):
        return f'{self.kind_of_sport} {self.type_of_event} {self.count_of_people} {self.date} '