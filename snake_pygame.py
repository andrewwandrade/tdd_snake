import pygame
import os
from snake_logic import Snake

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

SPRITE_FILES = {
    'head_up': 'head_up.png',
    'head_down': 'head_down.png',
    'head_left': 'head_left.png',
    'head_right': 'head_right.png',
    'body_horizontal': 'body_horizontal.png',
    'body_vertical': 'body_vertical.png',
    'body_topleft': 'body_topleft.png',
    'body_topright': 'body_topright.png',
    'body_bottomleft': 'body_bottomleft.png',
    'body_bottomright': 'body_bottomright.png',
    'tail_up': 'tail_up.png',
    'tail_down': 'tail_down.png',
    'tail_left': 'tail_left.png',
    'tail_right': 'tail_right.png',
    'fruit': 'apple.png',
}

CELL_SIZE = 32
FPS = 10

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

DIRECTION_NAME = {
    (1, 0): 'right',
    (-1, 0): 'left',
    (0, -1): 'up',
    (0, 1): 'down',
}

TURN_MAP = {
    ((1,0), (0,1)): 'body_topright',
    ((0,1), (1,0)): 'body_topright',
    ((-1,0), (0,1)): 'body_topleft',
    ((0,1), (-1,0)): 'body_topleft',
    ((1,0), (0,-1)): 'body_bottomright',
    ((0,-1), (1,0)): 'body_bottomright',
    ((-1,0), (0,-1)): 'body_bottomleft',
    ((0,-1), (-1,0)): 'body_bottomleft',
}

def direction(a: tuple, b: tuple, width: int, height: int) -> tuple:
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    if dx > width // 2: dx -= width
    if dx < -width // 2: dx += width
    if dy > height // 2: dy -= height
    if dy < -height // 2: dy += height
    return (dx, dy)

def get_segment_type(prev, current, next_seg, width: int, height: int) -> str:
    if prev is None and next_seg is None:
        return 'head_right'  

    if prev is None:
        d = direction(current, next_seg, width, height)
        return f"head_{DIRECTION_NAME[d]}"

    if next_seg is None:
        d = direction(prev, current, width, height)
        return f"tail_{DIRECTION_NAME[d]}"

    d_in  = direction(prev, current, width, height)
    d_out = direction(current, next_seg, width, height)

    if d_in == d_out:
        return 'body_horizontal' if d_in[0] != 0 else 'body_vertical'

    return TURN_MAP[(d_in, d_out)]

def load_assets(cell_size: int) -> dict:
    assets = {}
    for key, filename in SPRITE_FILES.items():
        path = os.path.join(ASSETS_DIR, filename)
        if os.path.exists(path):
            img = pygame.image.load(path)
            assets[key] = pygame.transform.scale(img, (cell_size, cell_size))
        else:
            assets[key] = None
    return assets

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
        self.assets = load_assets(cell_size)

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
            self.draw_sprite_or_color(fx, fy, 'fruit', COLOR_FRUIT)

        body = game.body
        n = len(body)

        for i, (bx, by) in enumerate(body):
            prev = body[i - 1] if i > 0 else None
            next_seg = body[i + 1] if i < n - 1 else None

            seg_type = get_segment_type(
                prev, (bx, by), next_seg, self.width, self.height
            )
            color = COLOR_SNAKE_HEAD if i == 0 else COLOR_SNAKE_BODY
            self.draw_sprite_or_color(bx, by, seg_type, color)
    
    def draw_sprite_or_color(self, x: int, y: int, key: str, fallback_color: tuple):
        sprite = self.assets.get(key)
        if sprite:
            self.screen.blit(sprite, (x * self.cell_size, y * self.cell_size))
        else:
            self.draw_cell(x, y, fallback_color)

    def draw_score(self, score: int):
        surf = self.font_small.render(f"Pontos: {score}", True, COLOR_TEXT)
        self.screen.blit(surf, (8, 8))
    
    def draw_centered_text(self, text: str, font, color: tuple, cy: int):
        surf = font.render(text, True, color)
        cx   = self.screen.get_width() // 2
        self.screen.blit(surf, surf.get_rect(center=(cx, cy)))

    def draw_game_over(self, score: int):
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        cy = self.screen.get_height() // 2
        self.draw_centered_text("GAME OVER", self.font_big, (220, 60, 60), cy - 40)
        self.draw_centered_text(f"Pontuação final: {score}", self.font_small, COLOR_TEXT, cy + 10)
        self.draw_centered_text("Pressione ESC para sair", self.font_small, (160, 160, 160), cy + 45)

    def flip(self):
        pygame.display.flip()

    def tick(self, fps: int = FPS):
        self.clock.tick(fps)
    
    def wait_for_exit(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

    def quit(self):
        pygame.quit()

def game_loop():
    DIM = (20, 15)
    game = Snake(DIM[0], DIM[1])
    renderer = PygameRenderer(width=DIM[0], height=DIM[1])

    last_direction = 'w'

    while True:
        cmd = renderer.poll_events()
        if cmd == 'end':
            break
        if cmd is not None:
            last_direction = cmd

        game.move(last_direction)

        if not game.alive:
            renderer.build_frame(game)
            renderer.draw_game_over(len(game.body))
            renderer.flip()
            renderer.wait_for_exit() 
            break

        renderer.build_frame(game)
        renderer.draw_score(len(game.body))
        renderer.flip()
        renderer.tick(FPS)

    renderer.quit()

if __name__ == "__main__":
    game_loop()