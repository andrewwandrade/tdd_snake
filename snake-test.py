from snake_logic import Snake

def test_snake_initial_position():
    game = Snake(20, 20)
    assert game.body == [(10, 10)]