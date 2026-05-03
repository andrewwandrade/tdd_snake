import pygame

CELL_SIZE = 32

KEY_MAP = {
    pygame.K_w: 'w',
    pygame.K_a: 'a',
    pygame.K_s: 's',
    pygame.K_d: 'd',
    pygame.K_ESCAPE: 'end',
}

class PygameRenderer:
    def __init__(self, width: int, height: int, cell_size: int = CELL_SIZE):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        pygame.init()
        self.screen = pygame.display.set_mode(
            (width * cell_size, height * cell_size)
        )
        pygame.display.set_caption("Snake")

        self.clock = pygame.time.Clock()
        self.font_big = pygame.font.SysFont("monospace", 36, bold=True)
        self.font_small = pygame.font.SysFont("monospace", 20)

    def translate_key(self, key: int):
        return KEY_MAP.get(key, None)

    def quit(self):
        pygame.quit()