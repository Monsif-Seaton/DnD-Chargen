from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class NewForm(FlaskForm):
    name = StringField('Name',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    clas = StringField('Class',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    race = StringField('Race',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    level = IntegerField('Level',
        validators = [
            DataRequired(),
        ]
    )
    CON = IntegerField('CON',
        validators = [
            DataRequired(),
        ]
    )
    DEX = IntegerField('DEX',
        validators = [
            DataRequired(),
        ]
    )
    STR = IntegerField('STR',
        validators = [
            DataRequired(),
        ]
    )
    INT = IntegerField('INT',
        validators = [
            DataRequired(),
        ]
    )
    WIS = IntegerField('WIS',
        validators = [
            DataRequired(),
        ]
    )
    CHA = IntegerField('CHA',
        validators = [
            DataRequired(),
        ]
    )
    Health = IntegerField('Health',
        validators = [
            DataRequired(),
        ]
    )
    Armor = IntegerField('Armor',
        validators = [
            DataRequired(),
        ]
    )
    Spell_points = IntegerField('Spell points',
        validators = [
            
        ]
    )
    Speed = IntegerField('Speed',
        validators = [
            DataRequired(),
        ]
    )
    submit = SubmitField('Create')
