import pygame
import itertools
import sieve
import os

pygame.init()



class Spiral():

    def __init__(self):
        self.size = int(input("Enter size of Ulam Spiral: "))
        screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption('Ulam Spiral')
        os.environ['SDL_VIDEO_CENTERED'] = '1'
    
        self.ns = self.get_primes(self.size)
        self.coords = []
        self.get_numbers()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0,0,0))


            for values in self.coords:
                screen.blit(values[0], values[1])

            pygame.display.flip()


    def get_numbers(self):
        x = y = 700 / 2 - 10
        dirs = itertools.cycle(['right','up','left','down'])
        d = next(dirs)
        times = 1
        j = 0
        temp = 0

        for i in range(self.size ** 2 + 1):
            if i < temp:
                continue
            for k in range(2):
                for l in range(times):
                    if temp in self.ns:
                        color = (255,0,255)
                    elif temp == 0:
                        color = (0,255,0)
                    else:
                        color = (250, 250, 210)

                    self.coords.append((self.blit_text('.', 25, color), (x, y)))
                    if d == 'right':
                        x += 500/self.size
                    elif d == 'up':
                        y -= 500/self.size
                    elif d == 'left':
                        x -= 500/self.size
                    elif d == 'down':
                        y += 500/self.size
                    temp += 1
                d = next(dirs)
            times += 1

    def blit_text(self, message, size, color):
        my_font = pygame.font.SysFont("kalinga", size)
        my_message = my_font.render(message, 0, color)

        return my_message

    def get_primes(self, n):
        return sieve.sieve(self.size ** 2)

def main():
    s = Spiral()

main()

