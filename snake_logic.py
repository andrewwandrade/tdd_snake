import random

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
        self.fruits = []
        self.update_fruits() 
        self.alive = True 

    def spawn_fruit(self):
        while True:
            new_fruit = (random.randint(0, self.width - 1), 
                         random.randint(0, self.height - 1))
            if new_fruit not in self.body and new_fruit not in self.fruits:
                self.fruits.append(new_fruit)
                break
    
    def update_fruits(self):
        target_count = (len(self.body)//10) + 1
        
        while len(self.fruits) < target_count:
            self.spawn_fruit()

    def _calculate_new_position(self, direction):
        dx, dy = MOVES[direction]
        x, y = self.body[0]
        return (x + dx) % self.width, (y + dy) % self.height

    def move(self, direction):
        if not self.alive or direction not in MOVES:
            return

        new_head = self._calculate_new_position(direction)

        if new_head in self.body:
            self.alive = False
            return 
        
        self.body.insert(0, new_head)

        if new_head in self.fruits:
            self.fruits.remove(new_head)
        else:
            self.body.pop()
        
        self.update_fruits()