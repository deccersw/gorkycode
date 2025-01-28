from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, IntegerField, SelectField, TimeField, TextAreaField
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
    count_of_people = IntegerField('Количество участников', validators=[DataRequired()]) # ползунок
    district =  SelectField('Район города', choices=[("Автозаводский район", "Автозаводский район"), ('Канавинский район', 'Канавинский район'),
                                                ('Ленинский район', 'Ленинский район'), ('Московский район', 'Московский район'),
                                                ('Сормовский район', 'Сормовский район'), ('Нижегородский район', 'Нижегородский район'), ('Приокский район', 'Приокский район'),
                                                ('Советский район', 'Советский район')],
                            validators=[DataRequired()])

    place =  SelectField('Спортивные площадки', choices=[("Территория Второго паркового озера", "Территория Второго паркового озера"), ('Территория парка «Дубки»', 'Территория парка «Дубки»'),
                                                ('Площадка на ул. Лопатина, д. 2, к.1', 'Площадка на ул. Лопатина, д. 2, к.1'), ('Бульвар Юбилейный, 30', 'Бульвар Юбилейный, 30'), ("Территория парка «Светлоярский»", "Территория парка «Светлоярский»"),
                                                ('ул. Акимова, 47', 'ул. Акимова, 47'), ('л. Сурикова-6', 'ул. Сурикова-6'), ('ул. Бекетова, 69', 'ул. Бекетова, 69'), ('ул. Ванеева, 106', 'ул. Ванеева, 106'),],
                            validators=[DataRequired()])
    date = StringField('Дата', validators=[DataRequired()])
    time = StringField('Время', validators=[DataRequired()])
    description = TextAreaField("Descr")
    submit = SubmitField("Опубликовать")
