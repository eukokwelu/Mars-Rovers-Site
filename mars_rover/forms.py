from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from wtforms.fields import DateField

"""
This was an attempt at a validator for submitting the date. Not cracked it yet :(
def rover_available_dates(rover, field):
    rover_dates = {'curiosity': '01-01-2015'}
    message = 'not quite right'

    def _check(form, field):
        selected = datetime.strptime(field.data, "%d-%m-%Y")
        present = datetime.now()
        if present.date() > selected.date() > rover_dates[rover]:
            return _check
        else:
            return ValidationError()
"""


class DateSubmissionForm(FlaskForm):
    Rover = SelectField(
        choices=[("Curiosity"), ("Perseverance"), ("Opportunity"), ("Spirit")],
        validators=[DataRequired()],
    )
    Date = DateField(validators=[DataRequired()], format="%Y-%m-%d")
    submit = SubmitField("Find")
