#!/usr/bin/env python3
#server/seed.py
from random import choice as rc
from faker import Faker
from app import app
from models import db, Pet

with app.app_context():
    fake=Faker()
    Pet.query.delete()
    # Create an empty list
    pets = []
    species=['Dog','Cat',"chicken",'Hamster','Turtle']
    # Add some Pet instances to the list
    for n in range(10):
        pets.append(Pet(name = fake.first_name(), species = rc(species)))

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()