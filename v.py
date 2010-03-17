import math

class Vector(list):
	def __init__(self, *args):
		if len(args) == 1 and type(args[0]) == list:
			list.__init__(self, args[0])
		else:
			for x in args:
				self.append(x)
		for i in range(len(self)):
			self[i] = float(self[i])

	def __add__(self, o):
		if type(o) == Vector:
			if len(self) == len(o):
				r = Vector()
				for i in range(len(self)):
					r.append(self[i] + o[i])
				return r
			else:
				raise Exception("Vectors are not equal size")
		else:
			raise TypeError("Only a Vector can be added to a Vector")

	def __iadd__(self, o):
		return self + o

	def __mul__(self, o):
		if type(o) == int or type(o) == float or type(o) == long:
			return Vector([ x*o for x in self ])
		else:
			raise TypeError("Only a scalar can be multiplied with a vector. To multiply two vectors, use .dot(o) or .cross(o)")

	def __imul__(self, o):
		return self * o

	def __div__(self, o):
		if type(o) == int or type(o) == float or type(o) == long:
			return Vector([ x/o for x in self ])
		else:
			raise TypeError("A Vector can only be divided by a scalar")

	def dot(self, o):
		if type(o) == Vector:
			if len(self) == len(o):
				r = 0
				for i in range(len(self)):
					r += self[i]*o[i]
				return r
			else:
				raise Exception("Vectors are not equal size")
		else:
			raise TypeError("Argument not Vector")

	def cross(self, o):
		if type(o) == Vector:
			a = self.pad(3)
			b = o.pad(3)
			return Vector([a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]])
		else:
			raise TypeError("Argument not Vector")

	def __abs__(self):
		r = 0
		for x in self:
			r += x**2
		return math.sqrt(r)

	def pad(self, n):
		r = Vector(self[:])
		while len(r) < n:
			r.append(0)
		return r

	def strip(self, n):
		r = Vector(self[:])
		while len(r) > n:
			r.pop()
		return r

	def null(self):
		for x in self:
			if x != 0:
				return False
		return True

	def __str__(self):
		return self.__repr__()
