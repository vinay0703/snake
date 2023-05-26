from Dependency.Di import Di
class Menu:
    def __init__(self):
        self.di = Di()

    def start(self):
        # input the play mode from the user
        self.printText(Di.constants.PLAY_MODE)
        play_mode_choice = int(input())
        if play_mode_choice == 1:
            self.printText(Di.constants.COMPUTER_PLAY_MODE)
            self.computer_play_mode()
        elif play_mode_choice == 2:
            self.printText(Di.constants.MANUAL_PLAY_MODE)
            self.manual_play_mode()
        else:
            self.printText(Di.constants.INVALID_PLAY_MODE)

    def computer_play_mode(self):
        pass

    def manual_play_mode(self):
        pass

    def printText(self, text):
        print(Di.constants.BREAK_LINE + text)

if __name__ == '__main__':
    menu = Menu()
    menu.start()