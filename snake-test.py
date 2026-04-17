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

def test_snake_wrap_around_horizontal():
    game = Snake(width=20, height=20)
    
    game.body = [(19, 10)]
    game.move('d') 

    assert game.body[0] == (0, 10)

def test_snake_wrap_around_vertical():
    game = Snake(width=20, height=20)
    
    game.body = [(10, 0)]
    game.move('w')

    assert game.body[0] == (10, 19)

def test_snake_grows_when_eating():
    game = Snake(20, 20)
    game.fruits = [(11, 10)] 
    game.move('d')
    assert len(game.body) == 2
    assert (11, 10) not in game.fruits

def test_multiple_fruits_at_size_10():
    game = Snake(20, 20)
    game.body = [(i, 0) for i in range(10)]
    game.update_fruits()
    assert len(game.fruits) == 2

def test_multiple_fruits_at_size_20():
    game = Snake(20, 20)
    game.body = [(i, 0) for i in range(20)]
    game.update_fruits()
    assert len(game.fruits) == 3

def test_collision_with_self_ends_game():
    game = Snake(20, 20)
    game.body = [(10, 10), (11, 10), (11, 11), (10, 11)]
    game.alive = True
    
    game.move('s')
    
    assert game.alive == False