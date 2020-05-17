from flask import render_template

from application import app

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
    return render_template("home.html", title="Home", chars=chars)

@app.route('/new')
def new():
 return render_template('new.html', title='New')

@app.route('/sheet/<name>')
def sheet(name):
    data = None
    if name in chars:
        data = chars[name]
    return render_template('sheet.html', title='Sheet',name=name, data=data, chars=chars)

@app.route("/edit")
def edit():
    return render_template('edit.html', title='Edit')
