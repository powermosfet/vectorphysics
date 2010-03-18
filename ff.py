import v, t, pygame

collisionK = 0.8
dragK = 1.7
gravityG = 9.81
normalThreshold = 0.0001
res = (0,0)
mouseK = 50
otherBallK = 10

def gravity(thing):
	g = gravityG
	return v.Vector(0, -(thing.mass * g))

def collision(thing):
	pos = thing.pos
	r = thing.r
	size = thing.size
	for i in (0, 1):
		if pos[i] + r > size[i]:
			thing.velocity[i] = -abs(thing.velocity[i])
			thing.velocity *= collisionK
		elif pos[i] - r < 0:
			thing.velocity[i] = abs(thing.velocity[i])
			thing.velocity *= collisionK
	return v.Vector(0,0)

def normal(thing):
	force = v.Vector(0,0)
	t = normalThreshold
	if thing.pos[1] - thing.r < t:
		force[1] = thing.mass * gravityG
	return force

def drag(thing):
	force = v.Vector(thing.velocity[0], thing.velocity[1])
	force *= -dragK
	return force

def mouse(thing):
	if pygame.mouse.get_pressed()[0]:
		pos = pygame.mouse.get_pos()
		pos = (float(pos[0])/res[0]*thing.size[0], float(res[1]-pos[1])/res[1]*thing.size[1])
		return v.Vector(mouseK*(pos[0]-thing.pos[0]), mouseK*(pos[1]-thing.pos[1]))
	else:
		return v.Vector(0,0)

def other(thing):
	r = v.Vector(otherBall.pos[0] - thing.pos[0], otherBall.pos[1] - thing.pos[1]) 
	r *= otherBallK
	return r

def other2(thing):
	r = v.Vector(otherBall2.pos[0] - thing.pos[0], otherBall2.pos[1] - thing.pos[1]) 
	r *= otherBallK
	return r
