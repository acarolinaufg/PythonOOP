from room import Room
from character import Enemy

kitchen = Room("Kitchen")
kitchen.set_description('A dank and dirty room buzzing with flies.')
#kitchen.describe()

dining_hall = Room("Dining Hall")
dining_hall.set_description('A beautiful place with the biggest sofa.')
#dining_hall.describe()

ballroom = Room("Ballroom")
ballroom.set_description('A amazing room.')
#ballroom.describe()

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

dave = Enemy("Dave", "A Smelly zombie")
dave.set_conversation('Brrlgrh....rgrhl....brains...')
dave.set_weakness('banana')
current_room = kitchen          

while True:		
    print("\n")         
    current_room.get_details() 
    inhabitant = current_room.get_character()
    if inhabitant is not None:
         inhabitant.describe()       
    command = input("> ")    
    current_room = current_room.move(command) 