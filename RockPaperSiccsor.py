import random

class Game:
    def __init__(self) -> None:
        self.user_input = ''
        self.choices = ['rock', 'paper', 'scissors']
        self.computer_choice = ''
    
    def get_computer_choice(self):
        self.computer_choice = random.choice(self.choices)
        return self.computer_choice
    
    def get_user_input(self):
        self.user_input = input("Rock, paper or scissors: ").lower()
        while self.user_input not in self.choices:
            print("Invalid input, try again")
            self.user_input = input("Rock, paper or scissors: ").lower()
    
    def play(self):
        self.get_user_input()
        computer = self.get_computer_choice()
        if self.user_input == computer:
            print(f"You played {self.user_input} and the computer played {computer}. It's a tie!")
        elif (self.user_input == 'rock' and computer == 'scissors') or \
             (self.user_input == 'paper' and computer == 'rock') or \
             (self.user_input == 'scissors' and computer == 'paper'):
            print(f"You played {self.user_input} and the computer played {computer}. You win!")
        else:
            print(f"You played {self.user_input} and the computer played {computer}. You lose!")
    
    def main(self):
        number = int(input("How many times do you want to play the game? "))
        for _ in range(number):
            self.play()

game = Game()
game.main()
