from character import Enemy
dave = Enemy('Dave','A smelly zombie')

dave.describe()

dave.set_conversation('Hi, guys!! Are everyone zombies here?')
dave.talk()
dave.set_weakness('banana')

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)