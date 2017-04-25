from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
from Dragon import Dragon
from random import randint

print ("What is thy name, brave adventurer?")
hero_name = raw_input("> ")
the_hero = Hero(hero_name)
# new_hero_name = raw_input("> ")
# the_new_hero = Hero(new_hero_name)

monsters = []
monsters_fighting = int(raw_input("How many monsters do you want to battle?"))
monsters_list = [Goblin(), Vampire(), Dragon()]

for i in range(0, monsters_fighting):
	list_index = randint(0, len(monsters_list) - 1)
	monsters.append(monsters_list[list_index])


# monsters.append(Goblin())
# monsters.append(Vampire())
# monsters.append(Dragon())

# print ("Welcome brave %s, you have encountered a goblin.") % the_hero.name - Do not 
# need this line of code because we want to randomize what monster we run into.

for monster in monsters:
	while monster.health > 0 and the_hero.is_alive():
		print "Brave %s, you have encountered a %s." % (the_hero.name, monster.name)
 		print "You have %d health and %d power." % (the_hero.health, the_hero.power)
 		print "The %s has %d health and %d power." % (monster.name, monster.health, monster.power)
 		print "What do you want to do?"
 		print "1. Fight %s" % monster.name
 		print "2. Do nothing"
 		print "3. Flee"
 		print "4. Drink potion of life"
 		print "> ",
 		user_input = raw_input()
 		if user_input == "1":
 			# hero to fight
 			# the_goblin.health -= the_hero.power

 			# the_hero.attack(the_goblin)
 			monster.take_damage(the_hero.power)

 			print "You have done %d damage to the %s." % (the_hero.power, monster.name) 
 			if monster.health <= 0:
 				print "You have defeated the %s!" % monster.name
 				the_hero.xp += monster.xp_value
 				the_hero.check_level()
 		elif user_input == "2":
 			#Hero is going to do nothing.
 			pass
		elif user_input == "3":
			print "Goodbye, coward"	
			break
		elif user_input == "4":
			the_hero.increase_health(20)
		else:
			print "invalid input %s" % user_input


		if monster.health > 0:
			the_hero.health -= monster.power
			print "The %s hits you for %d damage" % (monster.name, monster.power)
			if the_hero.health <= 0:
				print "You have been killed by the %s." % monster.name
				
				# the_hero.is_alive()
				# break
				print "Please choose a new character name: Bowie, Elvis, Jimmie"
				new_hero_name = raw_input("> ")
				the_new_hero = Hero(new_hero_name)

		if (the_hero.health > 0 and the_hero.health < 5):
			print "You have gone into a rage. Your power has increased!"
			the_hero.power += 5

