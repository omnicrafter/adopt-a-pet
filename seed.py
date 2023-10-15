from models import Pet, db
from app import app

db.drop_all()
db.create_all()

# Add pets
pet1 = Pet(name='Pikachu', species='Mouse',
           age=2, notes='Likes to shock people')
pet2 = Pet(name='Charmander', species='Lizard', age=4, notes='Breathes fire')
pet3 = Pet(name='Eevee', species='Fox', age=1, notes='Loves to play')
pet4 = Pet(name='Meowth', species='Cat', age=3, notes='Team Rocket')
pet5 = Pet(name='Psyduck', species='Duck', age=2, notes='Has a headache')
pet6 = Pet(name='Squirtle', species='Turtle', age=5, notes='Loves water')
pet7 = Pet(name='Bulbasaur', species='Dinosaur', age=6, notes='Likes to eat')
pet8 = Pet(name='Jigglypuff', species='Balloon', age=1, notes='Loves to sing')
pet9 = Pet(name='Snorlax', species='Bear', age=7, notes='Loves to sleep')
pet10 = Pet(name='Charizard', species='Dragon', age=8, notes='Breathes fire')

db.session.add_all([pet1, pet2, pet3, pet4, pet5,
                   pet6, pet7, pet8, pet9, pet10])

db.session.commit()
