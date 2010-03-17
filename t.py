import v, ff, pygame, sys

class Thing(object):
	def __init__(self,pos, mass, vInit, size, r):
		self.forces = []
		self.pygameEvents = []
		self.pos = pos
		self.mass = mass
		self.velocity = vInit
		self.size = size
		self.r = r

	def step(self, dt):
		netForce = v.Vector(0.0,0.0)
		for f in self.forces:
			netForce += f(self)
		acceleration = netForce / self.mass
		if abs(acceleration) > 0.1:
			self.velocity += (acceleration * dt)
		elif abs(self.velocity) < 0.2:
			self.velocity = v.Vector(0,0)
		self.pos += (self.velocity * dt)

	def getPos(self, res):
		x = int(self.pos[0]/self.size[0]*res[0])
		y = res[1] - int(self.pos[1]/self.size[1]*res[1])
		return (x, y)

	def __repr__(self):
		s  = "Pos: " + str(self.pos) + "\n"
		s += "Mass: " + str(self.mass) + "\n"
		s += "Velocity: " + str(self.velocity) + "\n"
		s += "Size: " + str(self.size) + "\n"
		return s

	def __str__(self):
		return self.__repr__()
