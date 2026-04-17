class Snake:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.body = [(width//2, height//2)]
    
    def move(self, direction):
        x, y = self.body[0]

        if direction == 'd':
            x+=1
        elif direction == 'a':
            x-=1
        elif direction == 'w':
            y+=1
        elif direction == 's':
            y-=1
        
        self.body = [(x, y)]