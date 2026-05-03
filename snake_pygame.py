import pygame

CELL_SIZE = 32
COLOR_BG = (15, 15, 15)
COLOR_SNAKE_HEAD = (80, 220, 80)
COLOR_SNAKE_BODY = (40, 160, 40)
COLOR_FRUIT = (220, 60, 60)
COLOR_GRID = (30, 30, 30)
COLOR_TEXT = (240, 240, 240)

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
    
    def poll_events(self) -> str | None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'end'
            if event.type == pygame.KEYDOWN:
                cmd = self.translate_key(event.key)
                if cmd is not None:
                    return cmd
        return None

    def draw_cell(self, x: int, y: int, color: tuple, shrink: int = 2):
        rect = pygame.Rect(
            x * self.cell_size + shrink,
            y * self.cell_size + shrink,
            self.cell_size - shrink * 2,
            self.cell_size - shrink * 2,
        )
        pygame.draw.rect(self.screen, color, rect, border_radius=4)

    def draw_grid(self):
        for col in range(self.width):
            for row in range(self.height):
                rect = pygame.Rect(
                    col * self.cell_size,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, COLOR_GRID, rect, 1)

    def build_frame(self, game):
        self.screen.fill(COLOR_BG)
        self.draw_grid()

        for fx, fy in game.fruits:
            self.draw_cell(fx, fy, COLOR_FRUIT, shrink=4)

        for i, (bx, by) in enumerate(game.body):
            color = COLOR_SNAKE_HEAD if i == 0 else COLOR_SNAKE_BODY
            self.draw_cell(bx, by, color)

    def draw_score(self, score: int):
        surf = self.font_small.render(f"Pontos: {score}", True, COLOR_TEXT)
        self.screen.blit(surf, (8, 8))
    
    def draw_game_over(self, score: int):
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        cx = self.screen.get_width()  // 2
        cy = self.screen.get_height() // 2

        title = self.font_big.render("GAME OVER", True, (220, 60, 60))
        score_surf = self.font_small.render(f"Pontuação final: {score}", True, COLOR_TEXT)
        hint = self.font_small.render("Pressione ESC para sair", True, (160, 160, 160))

        self.screen.blit(title, title.get_rect(center=(cx, cy - 40)))
        self.screen.blit(score_surf, score_surf.get_rect(center=(cx, cy + 10)))
        self.screen.blit(hint, hint.get_rect(center=(cx, cy + 45)))

    def quit(self):
        pygame.quit()