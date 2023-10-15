from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, connect_db, Pet
from flask_sqlalchemy import SQLAlchemy
# from flask_debugtoolbar import DebugToolbarExtension <-- causes Import error '_request_ctx_stack'
from flask_wtf import FlaskForm
from forms import AddPetForm
from functions import emptystr_to_none

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = "secretkey123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)
# app.app_context().push()

connect_db(app)
# db.create_all()


@app.route('/')
def home():
    """Redirect to /pets"""

    return redirect('/pets')


@app.route('/pets')
def list_pets():
    """Show all pets"""

    pets = Pet.query.all()

    return render_template('pets.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        # is this a post request? AND is the token valid?
        flash(f"Welcome {form.name.data}!")
        name = form.name.data
        species = form.species.data
        photo_url = emptystr_to_none(form.photo_url.data)
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species,
                      photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        return redirect('/pets')

    else:
        return render_template('add-pet-form.html', form=form)
