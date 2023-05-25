from snake.Dependency.Di import Di

class Menu:
    def __init__(self):
        self.di = Di()
        self.human_snake_game = self.di.human_snake_game
        self.pygame = self.di.pygame

    def start(self):
        # input the play mode from the user
        mode = "Select play mode ('1' for Computer and '2' for manual):\n"
        mode_choice = int(input(mode))

        if mode_choice == 1:
            print("Automatic computer play mode on")
        elif mode_choice == 2:
            print("Manual play mode on")
            self.human_play_mode()
        else:
            print("Invalid choice")

    def human_play_mode(self):
        self.di._init_pygame_functions()
        # game loop
        while True:
            game_over, score = self.human_snake_game.play_step()
            if game_over == True:
                break
        print('Final Score', score)

    def computer_play_mode(self):
        pass

if __name__ == '__main__':
    menu = Menu()
    menu.start()