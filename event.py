from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class CreateEvent(FlaskForm):
    kind_of_sport = StringField('Вид спорта', validators=[DataRequired()])
    type_of_event = StringField('Тип мероприятия', validators=[DataRequired()])
    count_of_people = IntegerField(validators=[DataRequired()])
    date = StringField('Дата', validators=[DataRequired()])
    time = StringField('Время', validators=[DataRequired()])
    place = StringField('Место', validators=[DataRequired()])
    submit = SubmitField("Создать")

    def __str__(self):
        return f'{self.kind_of_sport} {self.type_of_event} {self.count_of_people} {self.date} '

