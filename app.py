from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def show_homepage():
    """displays name, photo, and if available"""

    pets = Pet.query.all()

    return render_template('list_pets.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():
    """renders add pet form and handles submission"""

    form = PetForm()

    if form.validate_on_submit():
        """add to db"""
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>')
def show_pet_details(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet)

@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet_form(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect(f'/{pet_id}')
    else:
        return render_template('edit_pet_form.html', pet=pet, form=form)