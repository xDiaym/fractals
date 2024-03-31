from math import sin, cos, pi
from random import choice
from PIL import Image, ImageDraw

WIDTH, HEIGHT = 1920, 1080
ITERS, N, R, PHI = int(2e5), 3, min(WIDTH, HEIGHT) / 3, 1/2

X, Y = WIDTH // 2, HEIGHT // 2

def vertices(n: int, R: float) -> list[tuple[int, int]]:
    f = 2*pi/n
    return [
        (int(R * cos(f * i - pi/2) + X), int(R * sin(f * i - pi / 2) + Y))
        for i in range(n)
    ]

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def move_to(self, x2: int, y2: int, f: float) -> None:
        self.x = int((x2 - self.x) * f)
        self.y = int((y2 - self.y) * f)

p = Point(X, Y)
image = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))
pxl = image.load()
draw = ImageDraw.Draw(image)
vert = vertices(3, R)
for i in range(N):
    start, end = vert[i], vert[(i + 1) % N]
    draw.line((start, end), fill='blue', width=2)
for _ in range(ITERS):
    p2 = choice(vert)
    p.move_to(*p2, PHI)
    pxl[p.x, p.y] = (255, 255, 255)
image.show()
