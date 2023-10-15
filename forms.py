from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField, TextAreaField


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name")
    species = SelectField("Species", choices=[
                          ('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = TextAreaField("Notes")
