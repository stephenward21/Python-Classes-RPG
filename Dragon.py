class Dragon(object):
	def __init__ (self):
		self.health = 15
		self.power = 7
		self.name = "Dragon"
		self.xp_value = 12
	def take_damage(self, damage):
		self.health -= damage
	def is_alive (self):
		return self.health > 0
