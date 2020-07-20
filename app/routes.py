from flask import render_template, request, redirect
from app import app, db
from app.models import Entry


@app.route('/')
@app.route('/index')
def index():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        name = form.get('name')
        color = form.get('color')
        pet = form.get('pet')
        if not name or color:
            entry = Entry(name = name, color = color, pet = pet)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

    return "Success!"

@app.route('/delete/<string:name>')
def delete(name):
    if not name or name != None:
        entry = Entry.query.get(name)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return "Success!"


