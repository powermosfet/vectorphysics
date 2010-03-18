import v, t, ff, pygame

pygame.init()

#Resolution and framerate
res = (800, 600)
ff.res = res
framerate = 30
dt = 1.0/framerate
clock = pygame.time.Clock()

#Set up graphics
s = pygame.display.set_mode(res)
ball = pygame.image.load("ball.png")
black = ball.copy()
black.fill((0,0,0))
ballRect1 = ball.get_rect()
ballRect2 = ball.get_rect()

#Ball properties
pos = v.Vector(4,5)		#Position
m = 2					#Mass
vInit = v.Vector(3,0)	#Initial velocity
size = (8,6)			#Room size
r = 0.1					#Ball radius

#Create ball object and register force functions
tBall = t.Thing(pos, m, vInit, size, r)
tBall.forces.append(ff.gravity)
tBall.forces.append(ff.collision)
tBall.forces.append(ff.normal)
tBall.forces.append(ff.drag)
tBall.forces.append(ff.mouse)
tBall.forces.append(ff.other2)

ff.otherBall = tBall
ff.otherBallK = 15

#Create ball object and register force functions
uBall = t.Thing(pos, m, vInit*-1, size, r)
uBall.forces.append(ff.gravity)
uBall.forces.append(ff.drag)
uBall.forces.append(ff.normal)
uBall.forces.append(ff.collision)
uBall.forces.append(ff.other)

ff.otherBall2 = uBall

#Enter simulation loop
run = True
while run:
	for e in pygame.event.get():			#Exit if close button is clicked or a key is pressed
		if e.type == pygame.QUIT or e.type == pygame.KEYDOWN:
			run = False
	clock.tick(framerate)					#Wait until the next frame
	tBall.step(dt)							#Calculate next position
	uBall.step(dt)							#Calculate next position
	s.blit(black, ballRect1)					#Black out the old ball
	s.blit(black, ballRect2)					#Black out the old ball
	ballRect1.center = tBall.getPos(res)		#Set new position
	ballRect2.center = uBall.getPos(res)		#Set new position
	s.blit(ball, ballRect1)					#Draw the new ball
	s.blit(ball, ballRect2)					#Draw the new ball
	pygame.display.flip()					#Update the screen
