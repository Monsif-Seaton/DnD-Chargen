from flask import render_template, redirect, url_for
from application.models import characters
from application import app, db
from application.forms import NewForm

chars = {
        "Kaynon Song": {
        "name":"Kaynon Song",
        "class":"Warlock",
        "race":"Tiefling",
        "level":10,
        "CON":14,
        "DEX":13,
        "STR":9,
        "INT":11,
        "WIS":13,
        "CHA":18,
        "Health":73,
        "Armor":14,
        "Spell points":63,
        "Speed":30
    },
    "t4r9s": {
        "name": "t4r9s",
        "class": "Ranger",
        "race":"Warforged",
        "level":5,
        "CON":17,
        "DEX":19,
        "STR":9,
        "INT":8,
        "WIS":12,
        "CHA":6,
        "Health":47,
        "Armor":17,
        "Spell points":14,
        "Speed":35
    }
    }

@app.route("/")
@app.route("/home")
def home():
    Characters = characters.query.first()
    return render_template("home.html", title="Home", chars=chars, Characters=Characters)

@app.route('/new', methods=["GET", "POST"])
def new():
    form = NewForm()
    if form.validate_on_submit():
        new = characters(
name = form.name.data, clas = form.clas.data, race = form.race.data, level = form.level.data,CON = form.CON.data, DEX = form.DEX.data, STR = form.STR.data, INT = form.INT.data, WIS = form.WIS.data, CHA = form.CHA.data, Health = form.Health.data, Armor = form.Armor.data, Spell_points = form.Spell_points.data, Speed = form.Speed.data)
        db.session.add(new)
        db.session.commit()

        return redirect(url_for("home"))
    else:
        print(form.errors)

    return render_template("new.html", title="New", form=form)

@app.route('/sheet/<name>')
def sheet(name):
    data = None
    if name in chars:
        data = chars[name]
    return render_template('sheet.html', title='Sheet',name=name, data=data, chars=chars)

@app.route("/edit")
def edit():
    return render_template('edit.html', title='Edit')

