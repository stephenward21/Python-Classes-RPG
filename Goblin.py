from Monster import Monster
class Goblin(Monster):
	def __init__(self):
		self.health = 6
		self.power = 2
		self.name = "Goblin"
		self.xp_value = 5
	def take_damage(self, damage):
		self.health -= damage
	def is_alive(self):
		return self.health > 0