from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from wtforms.fields import DateField


class DateSubmissionForm(FlaskForm):
    Rover = SelectField(
        choices=[("Curiosity"), ("Perseverance"), ("Opportunity"), ("Spirit")],
        validators=[DataRequired()],
    )
    Date = DateField(validators=[DataRequired()], format="%Y-%m-%d")
    submit = SubmitField("Find")
