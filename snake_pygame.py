import pygame

CELL_SIZE = 32

class PygameRenderer:
    def __init__(self, width: int, height: int, cell_size: int = CELL_SIZE):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        pygame.init()
        self.screen = pygame.display.set_mode(
            (width * cell_size, height * cell_size)
        )

    def quit(self):
        pygame.quit()