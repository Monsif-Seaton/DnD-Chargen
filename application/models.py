from application import db

class characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    clas = db.Column(db.String(30), nullable=False)
    race = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    CON = db.Column(db.Integer, nullable=False)
    DEX = db.Column(db.Integer, nullable=False)
    STR = db.Column(db.Integer, nullable=False)
    INT = db.Column(db.Integer, nullable=False)
    WIS = db.Column(db.Integer, nullable=False)
    CHA = db.Column(db.Integer, nullable=False)
    Health = db.Column(db.Integer, nullable=False)
    Armor = db.Column(db.Integer, nullable=False)
    Spell_points = db.Column(db.Integer)
    Speed = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return ''.join([
            'Name: ', self.name, '\r\n ',
            "Class: ", self.clas, '\r\n',
            'Race: ', self.race, '\r\n',
            "Speed: ", self.Speed, '\r\n'
            ])
