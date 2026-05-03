import os
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