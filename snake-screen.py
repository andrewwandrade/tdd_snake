import os
import keyboard
import time
from snake_logic import Snake

class io_handler:
    
    x_size: int
    y_size: int
    game_speed = float
    last_input: str
    matrix = []

    def __init__(self, dim, speed):
        self.x_size = dim[0]
        self.y_size = dim[1]
        
        self.game_speed = speed
        self.last_input = 'w'

        for i in range (self.y_size): 
            self.matrix.append([0]*self.x_size)

    def record_inputs(self):
        keyboard.add_hotkey('w', lambda: setattr(self, "last_input", 'w'))
        keyboard.add_hotkey('a', lambda: setattr(self, "last_input", 'a'))
        keyboard.add_hotkey('s', lambda: setattr(self, "last_input", 's'))
        keyboard.add_hotkey('d', lambda: setattr(self, "last_input", 'd'))
        keyboard.add_hotkey('esc', lambda: setattr(self, "last_input", 'end'))

    def display(self):
        def display_h_line(self):
            print ('+', end='')
            print ('--'* len(self.matrix[0]), end='')
            print ('+')
        
        def display_content_line(line):
            print ('|', end='')
            for item in line: 
                if item == 1:
                    print ('[]', end='')
                elif item == 2:
                    print ('<>', end='')
                elif item == 3:
                    print ('()', end='')
                else:
                    print ('  ', end='')

            print ('|')

        os.system('cls' if os.name == 'nt' else 'clear')
        display_h_line(self)
        for line in self.matrix:
            display_content_line(line)
        display_h_line(self)

def game_loop():
    #Configurações de inicialização do jogo
    dim = (10, 15)
    speed = 0.3
    instance = io_handler(dim, speed)
    game = Snake(dim[0], dim[1])
    
    instance.record_inputs()
    
    while True:
        for y in range(instance.y_size):
            for x in range(instance.x_size):
                instance.matrix[y][x] = 0   

        game.move(instance.last_input)
        
        if not game.alive:
            pontuacao_final = len(game.body)
            print("\n")
            print("="*21)
            print("GAME OVER!")
            print(f"PONTUAÇÃO FINAL: {pontuacao_final}")
            print("="*21)
            print("\n")
            break

        for fruit_x, fruit_y in game.fruits:
            instance.matrix[fruit_y][fruit_x] = 3
        for i, (body_x, body_y) in enumerate(game.body):
            instance.matrix[body_y][body_x] = 2 if i == 0 else 1
        
        instance.display()
        print(f"Pontos: {len(game.body)} | ", end='') 
        print("mova com WASD, saia com esc. Ultimo botão:", end=' ')

        print(instance.last_input)
        if(instance.last_input == 'end'):
            exit()
        time.sleep(instance.game_speed)

game_loop()