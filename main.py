import pygame, random
from time import sleep

class droplet(object):
    def __init__(self, color, x, y, w, h):
        self.x = x
        self.y = y
        self.rect = pygame.Surface((w,h))
        self.rect.fill(color)
    def update(self):
        self.y += 8
        if self.y > 480:
            self.y = random.randint(0, 1)
            self.x = random.randint(10, 600)
    def draw(self, window):
        window.blit(self.rect, (self.x, self.y))
        
def quitEvent(event):
    if event.type == pygame.QUIT:
        return False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            return False
    else:
        return True

def main():
    pygame.init()
    windowSize = (640, 480)
    window = pygame.display.set_mode(windowSize)
    rects = []
    droplets = 200
    for i in range(droplets):
        rect = droplet((0,150,255), random.randint(5, 639), -abs(random.randint(10, 500)), 2, 20)
        rects.append(rect)
    running = True
    while running:
        for event in pygame.event.get():
            running = quitEvent(event)
        window.fill(0)
        for i in range(droplets):
            rects[i].update()
            rects[i].draw(window)
        pygame.display.update()
        sleep(10/1000)
main()

