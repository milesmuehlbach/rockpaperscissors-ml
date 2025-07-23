import random
import time
import pyfiglet
from . import fetchsign

# Terminal color codes
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class RPSGame:
    def __init__(self):
        self.signs = ["rock", "paper", "scissors"]
        self.banner()
        print("When prompted, please hold your sign up to the camera to allow it to be captured.\n")

    def banner(self):
        title = pyfiglet.figlet_format("Rock Paper Scissors")
        print(f"{Colors.OKBLUE}{title}{Colors.ENDC}")

    def rpss(self):
        print("Ready? (Get your sign ready...)")
        time.sleep(1)
        print("Rock...")
        time.sleep(0.5)
        print("Paper...")
        time.sleep(0.5)
        print("Scissors...")
        time.sleep(0.5)
        print("Shoot! (Hold your sign for a second as we fetch it...)")

    def decide_winner(self, user, computer):
        if user == computer:
            return "tie"
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            return "win"
        return "lose"

    def play(self):
        while True:
            input("Press Enter to continue...")
            self.rpss()

            print("\nFetching your sign from the camera...")
            while True:
                user_sign = fetchsign.fetch()
                if user_sign != "unknown":
                    break
                print(f"{Colors.WARNING}Could not recognize your sign. Try again.{Colors.ENDC}")

            computer_sign = random.choice(self.signs)

            print(f"\nYour sign: {Colors.OKGREEN}{user_sign.upper()}{Colors.ENDC}")
            print(f"Computer's sign: {Colors.FAIL}{computer_sign.upper()}{Colors.ENDC}")

            result = self.decide_winner(user_sign, computer_sign)
            if result == "tie":
                print(f"{Colors.WARNING}It's a tie!{Colors.ENDC}")
            elif result == "win":
                print(f"{Colors.OKGREEN}You win!{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}You lose!{Colors.ENDC}")

            print()
            again = input("Play again? (y/n): ").strip().lower()
            if again != 'y':
                print(f"{Colors.BOLD}Thanks for playing!{Colors.ENDC}")
                break

if __name__ == "__main__":
    game = RPSGame()
    game.play()
