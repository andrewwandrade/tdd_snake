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

    def _calculate_new_position(self, direction):
        dx, dy = MOVES[direction]
        x, y = self.body[0]
        return (x + dx) % self.width, (y + dy) % self.height

    def move(self, direction):
        if direction in MOVES:
            new_head = self._calculate_new_position(direction)
            self.body = [new_head]