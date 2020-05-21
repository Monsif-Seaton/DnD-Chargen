from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields import SelectField
from wtforms.validators import DataRequired, Length

class NewForm(FlaskForm):
    name = StringField('Name',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    clas = SelectField('Class', choices=[("Barbarian","Barbarian"),("Bard","Bard"),("Cleric","Cleric"),("Druid","Druid"),("Fighter","Fighter"),("Monk","Monk"),("Paladin","Paladin"),("Ranger","Ranger"),("Rogue","Rogue"),("Sorcerer","Sorcerer"),("Warlock","Warlock"),("Wizard","Wizard")]
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

class EditForm(FlaskForm):
    name = StringField('Name',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    clas = SelectField('Class', choices=[("Barbarian","Barbarian"),("Bard","Bard"),("Cleric","Cleric"),("Druid","Druid"),("Fighter","Fighter"),("Monk","Monk"),("Paladin","Paladin"),("Ranger","Ranger"),("Rogue","Rogue"),("Sorcerer","Sorcerer"),("Warlock","Warlock"),("Wizard","Wizard")]
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
    submit = SubmitField('Update')

class DeleteForm(FlaskForm):
    submit = SubmitField("Delete this character")
