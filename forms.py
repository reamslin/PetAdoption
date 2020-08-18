from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class PetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet's Name",
    validators=[InputRequired()])
    species = StringField("Pet's Species",
    validators=[InputRequired(), AnyOf(['cat', 'dog', 'rabbit', 'frog'],
    message="we only accept cats, dogs, rabbits, and frogs")])
    photo_url = StringField("URL of Pet's Image",
    validators=[Optional()])
    age = IntegerField("Age of Pet",
    validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Additional Notes")
    available = BooleanField("Is this pet available for adoption?")
