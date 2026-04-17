MOVES = {
    'w': (0, -1),
    's': (0, 1),
    'a': (-1, 0),
    'd': (1, 0)
}

class Snake:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.body = [(width//2, height//2)]

    def move(self, direction):
        dx, dy = MOVES[direction]
        x, y = self.body[0]
        self.body = [(x + dx, y + dy)]