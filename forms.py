from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Email, AnyOf, NoneOf


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[
                       InputRequired(message="Pet name cannot be blank")])
    species = RadioField("Species", choices=[
        ('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'], message="Species must be cat, dog, or porcupine")])
    photo_url = StringField("Photo URL", validators=[
                            Optional(), URL(message="Please enter a valid URL")])
    age = IntegerField("Age", validators=[
                       Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = TextAreaField("Notes", validators=[Optional()])


class PetForm(FlaskForm):
    """Form for editing pets."""
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Pet name cannot be blank")])
    species = RadioField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[
                         InputRequired(), AnyOf(['cat', 'dog', 'porcupine'], message="Species must be cat, dog, or porcupine")])
    photo_url = StringField("Photo URL", validators=[
                            Optional(), URL(message="Please enter a valid URL")])
    age = IntegerField("Age", validators=[
                       Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = TextAreaField("Notes", validators=[Optional()])
