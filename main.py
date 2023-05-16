from random import randrange
import pygame

WIDTH = 800
HEIGHT = 800
CENTER = WIDTH / 2, HEIGHT / 2
centerX = WIDTH / 2
centerY = HEIGHT / 2
FPS = 60

GRAVITY = 0.5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

particles = []
voids = []

Vector2 = pygame.math.Vector2
clock = pygame.time.Clock()


class Particle:
    def __init__(self, x, y):
        self.grav = GRAVITY
        self.vel = Vector2(-8, 8)
        self.x = x
        self.y = y
        self.slack = 1

    def move(self, central):
        dir_vec = Vector2(centerX, centerY) - (self.x, self.y) # gets direction between 0 - 1
        v_len_sq = dir_vec.length_squared() # gets distance to center
        if v_len_sq > 0:
            dir_vec.scale_to_length(self.grav) # flips sign to keep rotation
            self.vel = (self.vel + dir_vec) * self.slack # velocity calculation
            self.x += self.vel.x # add velocity to x
            self.y += self.vel.y # add velocity to y
        return [self.x, self.y]


def black_hole():
    b = Particle(centerX, centerY)
    b.v = 0
    voids.append(b)


def generator():
    for i in range(1000):
        x = randrange(100,400)
        y = randrange(100,400)
        p = Particle(x, y)
        particles.append(p)


black_hole()
generator()


def draw():
    for i in range(len(voids)):
        pygame.draw.circle(screen, RED, CENTER, 30)
    for i in range(len(particles)):
        pygame.draw.circle(screen, WHITE, (particles[i].move(CENTER)), 5)


running = True
while running:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    draw()

    pygame.display.update()
