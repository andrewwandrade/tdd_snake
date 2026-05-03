import os
import pygame
from snake_logic import Snake
from snake_pygame import get_segment_type
from snake_pygame import load_assets

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

def test_draw_game_over():
    pygame.init()
    renderer = PygameRenderer(width=10, height=10, cell_size=20)
    renderer.build_frame(Snake(10, 10))
    renderer.draw_game_over(3)
    renderer.quit()

def test_flip_not_exception():
    pygame.init()
    renderer = PygameRenderer(width=10, height=10, cell_size=20)
    renderer.build_frame(Snake(10, 10))
    renderer.flip()
    renderer.quit()

def test_tick_not_exception():
    pygame.init()
    renderer = PygameRenderer(width=10, height=10, cell_size=20)
    renderer.tick(60)
    renderer.quit()

def test_head_direita():
    assert get_segment_type(None, (5,5), (6,5), 20, 20) == 'head_right'

def test_head_baixo():
    assert get_segment_type(None, (5,5), (5,6), 20, 20) == 'head_down'

def test_body_horizontal():
    assert get_segment_type((3,5), (4,5), (5,5), 20, 20) == 'body_horizontal'

def test_body_vertical():
    assert get_segment_type((5,3), (5,4), (5,5), 20, 20) == 'body_vertical'

def test_tail_direita():
    assert get_segment_type((5,5), (6,5), None, 20, 20) == 'tail_right'

def test_head_wrap_horizontal():
    assert get_segment_type(None, (19,5), (0,5), 20, 20) == 'head_right'

def test_load_assets_returns_dictionary():
    pygame.init()
    assets = load_assets(cell_size=32)
    assert isinstance(assets, dict)

def test_load_assets_contains_required_keys():
    pygame.init()
    assets = load_assets(cell_size=32)
    chaves = [
        'head_up', 'head_down', 'head_left', 'head_right',
        'body_horizontal', 'body_vertical',
        'body_topleft', 'body_topright',
        'body_bottomleft', 'body_bottomright',
        'tail_up', 'tail_down', 'tail_left', 'tail_right',
        'fruit',
    ]
    for chave in chaves:
        assert chave in assets, f"chave ausente: {chave}"

def test_load_assets_values_are_surface_or_none():
    pygame.init()
    assets = load_assets(cell_size=32)
    for key, val in assets.items():
        assert val is None or isinstance(val, pygame.Surface), \
            f"{key} deveria ser Surface ou None, é {type(val)}"