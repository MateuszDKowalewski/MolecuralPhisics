import math
import random
import sys
import pygame


class Simulation:

    def __init__(self):
        self.screen = pygame.display.set_mode((900, 500))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Molecular simulation")
        self.atoms = []

        for i in range(0, 100):
            self.atoms.append(Atom())

        # self.atoms.append(Atom((150, 150)))
        # self.atoms.append(Atom((200, 200)))

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                self.handle_quit_event(event)
            for atom in self.atoms:
                atom.calculate_velocity(self.atoms)
            for atom in self.atoms:
                atom.tick()
            self.draw()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for atom in self.atoms:
            atom.draw(self.screen)
        pygame.display.flip()

    def handle_quit_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


class Atom:

    def __init__(self):
        self.position = (random.randint(0, 900), random.randint(0, 500))
        self.velocity = (0, 0)
        self.color = (255, 0, 0)

    # def __init__(self, position):
    #     self.position = position
    #     self.velocity = (0, 0)
    #     self.color = (255, 0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, 2)

    def tick(self):
        self.position = (self.position[0] + self.velocity[0] / 60, self.position[1] + self.velocity[1] / 60)

    def calculate_velocity(self, atoms):
        for atom in atoms:
            if self != atom:
                dx = atom.position[0] - self.position[0]
                dy = atom.position[1] - self.position[1]
                self.velocity = (self.velocity[0] + 1 / dx, self.velocity[1] + 1 / dy)


if __name__ == "__main__":
    Simulation()
