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
ballRect = ball.get_rect()

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

#Initially display the ball, then enter simulation loop
s.blit(ball, ballRect)
pygame.display.flip()
run = True
while run:
	for e in pygame.event.get():			#Exit if close button is clicked or a key is pressed
		if e.type == pygame.QUIT or e.type == pygame.KEYDOWN:
			run = False
	clock.tick(framerate)					#Wait until the next frame
	tBall.step(dt)							#Calculate next position
	s.blit(black, ballRect)					#Black out the old ball
	ballRect.center = tBall.getPos(res)		#Set new position
	s.blit(ball, ballRect)					#Draw the new ball
	pygame.display.flip()					#Update the screen
