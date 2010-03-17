import v, t, ff, pygame

pygame.init()

res = (800, 600)
framerate = 30

s = pygame.display.set_mode(res)
ball = pygame.image.load("ball.png")
black = ball.copy()
black.fill((0,0,0))
ballRect = ball.get_rect()
clock = pygame.time.Clock()
dt = 1.0/framerate

tBall = t.Thing(v.Vector(4,5), 2, v.Vector(3,0), (8, 6), 0.1)
tBall.forces.append(ff.gravity)
tBall.forces.append(ff.collision)
tBall.forces.append(ff.normal)
tBall.forces.append(ff.drag)
tBall.forces.append(ff.mouse)

ff.res = res

s.blit(ball, ballRect)
pygame.display.flip()
run = True
while run:
	for e in pygame.event.get():
		if e.type == pygame.QUIT or e.type == pygame.KEYDOWN:
			run = False
	clock.tick(framerate)
	tBall.step(dt)
	s.blit(black, ballRect)
	ballRect.center = tBall.getPos(res)
	s.blit(ball, ballRect)
	pygame.display.flip()
