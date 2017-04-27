from Hero import Hero
from Vampire import Vampire
from Monster import Goblin
from Monster import Dragon
from random import randint
from New_Character import New_Character



print ("What is thy name, brave adventurer?")
hero_name = raw_input("> ")
the_hero = Hero(hero_name)


monsters = []
monsters_fighting = int(raw_input("How many monsters do you want to battle?"))
monsters_list = [Goblin(), Vampire()]


for i in range(0, monsters_fighting):
	list_index = randint(0, len(monsters_list) - 1)
	monsters.append(monsters_list[list_index])


#  
# 
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
 		print "5. Go to the shop!"
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
	

		elif user_input == "5":
			print "Pick your heart's desire!"
			print "1. Bow and arrow"
			print "2. Giant Sword"
			print "3. Poison darts"
			print "4. Mind/Body altering potions"
			hero_choice = raw_input("> ")
			if hero_choice == "1":
				the_hero.power += 2
				print "Your power has increased to %d!\n" % the_hero.power
			elif hero_choice == "2":
				the_hero.power += 3
			elif hero_choice == "3":
				the_hero.power += 4
				print "Your health has increased to %d!\n" % the_hero.health
			elif hero_choice == "4":
				the_hero.health += randint(-5, 5)
			

		else:
			print "invalid input %s" % user_input

		if monster.health > 0:
			the_hero.health -= monster.power
			print "The %s hits you for %d damage" % (monster.name, monster.power)
			if the_hero.health <= 0:
				print "You have been killed by the %s." % monster.name
				continue_game = raw_input("Would you like to start a new game (Y/N)")
				if continue_game == "Y":
					new_hero = raw_input("Please pick a new character: Bowie or Prince?")
					the_hero.is_alive()
					if new_hero == "Bowie":
						bowie = New_Character("Bowie", "Mars", "Battle-axe")
						print ("You are now on %s, and your new weapon is a %s") % (bowie.region, bowie.weapon)
						bowie.new_screen()
						
					elif new_hero == "Prince":
						prince = New_Character("Prince", "Lake Minnetonka", "Shredder")
						print ("You are now on %s, and your new weapon is a %s") % (prince.region, prince.weapon)
						prince.new_screen()

				if continue_game == "N":
					print ("You are a loser!")



				# the_hero.is_alive()
				# break
				# print "Please choose a new character name: Bowie, Elvis, Jimmie"
				# new_hero_name = raw_input("> ")
				# the_new_hero = Hero(new_hero_name)

		if (the_hero.health > 0 and the_hero.health < 5):
			print "You have gone into a rage. Your power has increased!"
			the_hero.power += 5

