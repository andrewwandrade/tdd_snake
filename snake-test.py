from snake_logic import Snake

def test_snake_initial_position():
    game = Snake(20, 20)
    assert game.body == [(10, 10)]

def test_snake_moves_right():
    game = Snake(20, 20)
    game.move('d') 
    assert game.body[0] == (11, 10)

def test_snake_moves_left():
    game = Snake(20, 20)
    game.move('a') 
    assert game.body[0] == (9, 10)

def test_snake_moves_up():
    game = Snake(20, 20)
    game.move('w') 
    assert game.body[0] == (10, 9)

def test_snake_moves_down():
    game = Snake(20, 20)
    game.move('s') 
    assert game.body[0] == (10, 11)