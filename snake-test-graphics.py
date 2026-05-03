import os
import pygame
from snake_logic import Snake

os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"

from snake_pygame import PygameRenderer, CELL_SIZE

def test_renderer_starts_without_error():
    renderer = PygameRenderer(width=10, height=10, cell_size=CELL_SIZE)
    renderer.quit()

def test_renderer_correct_dimensions():
    renderer = PygameRenderer(width=10, height=10, cell_size=20)
    assert renderer.screen.get_width()  == 10 * 20
    assert renderer.screen.get_height() == 10 * 20
    renderer.quit()

def test_translate_key_wasd():
    pygame.init()
    renderer = PygameRenderer(width=10, height=10, cell_size=20)
    assert renderer.translate_key(pygame.K_w) == 'w'
    assert renderer.translate_key(pygame.K_a) == 'a'
    assert renderer.translate_key(pygame.K_s) == 's'
    assert renderer.translate_key(pygame.K_d) == 'd'
    assert renderer.translate_key(pygame.K_ESCAPE) == 'end'
    renderer.quit()

def test_translate_unknown_key_returns_none():
    pygame.init()
    renderer = PygameRenderer(width=10, height=10, cell_size=20)
    assert renderer.translate_key(pygame.K_z) is None
    renderer.quit()

def test_build_frame_does_not_raise_exception():
    pygame.init()
    renderer = PygameRenderer(width=10, height=10, cell_size=20)
    game = Snake(10, 10)
    renderer.build_frame(game) 
    renderer.quit()

def test_build_frame_snake_with_multiple_segments():
    pygame.init()
    renderer = PygameRenderer(width=20, height=20, cell_size=20)
    game = Snake(20, 20)
    game.body = [(5, 5), (4, 5), (3, 5)]
    renderer.build_frame(game)
    renderer.quit()

def test_draw_score():
    pygame.init()
    renderer = PygameRenderer(width=10, height=10, cell_size=20)
    renderer.build_frame(Snake(10, 10))
    renderer.draw_score(5)
    renderer.quit()