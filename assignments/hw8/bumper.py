"""
Name: Eton Cheng
bumper.py

Problem: 2 bumper cars altering directions upon collisions

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import pygame

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

x1 = 200
y1 = 200
r1 = 50
mx1 = 2
my1 = 0.5
x2 = 300
y2 = 200
r2 = 50
mx2 = -1
my2 = -1.5


def move(c, v, r, m):
    c += v
    if c < r:
        c, v = r, -v
    if c > m-r:
        c, v = m-r, -v
    return c, v


while True:
    clock.tick(70)
    x1, mx1 = move(x1, mx1, r1, 500)
    y1, my1 = move(y1, my1, r1, 500)
    x2, mx2 = move(x2, mx2, r2, 500)
    y2, my2 = move(y2, my2, r2, 500)
    v1 = pygame.math.Vector2(x1, y1)
    v2 = pygame.math.Vector2(x2, y2)
    if v1.distance_to(v2) < r1 + r2 - 2:
        nv = v2 - v1
        m1 = pygame.math.Vector2(mx1, my1).reflect(nv)
        m2 = pygame.math.Vector2(mx2, my2).reflect(nv)
        mx1, my1 = m1.x, m1.y
        mx2, my2 = m2.x, m2.y
    window.fill((255, 255, 255))
    pygame.draw.circle(window, (255, 0, 0), (round(x1), round(y1)), r1, 3)
    pygame.draw.circle(window, (0, 0, 255), (round(x2), round(y2)), r2, 3)
    pygame.display.flip()
