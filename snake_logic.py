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
        if direction not in MOVES:
            return

        dx, dy = MOVES[direction]
        x, y = self.body[0]

        new_x = (x + dx) % self.width
        new_y = (y + dy) % self.height
        
        self.body = [(new_x, new_y)]