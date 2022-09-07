"""PJ00 Guess The Number!"""

__author__ = "730401629"


player: str = "player name"
points: int

# Constants for Emojis
BLUE_DIAMOND: str = '\U0001F537'
EXIT: str = '\U0001F3C1'
GREEN_SQUARE: str = '\U0001F7E9'
YELLOW_SQUARE: str = '\U0001F7E8'
RED_SQUARE: str = '\U0001F7E5'
UP: str = '\U0001F446'
BLUE_CIRCLE: str = '\U0001F535'
SMILE: str = '\U0001F603'
STAR: str = '\U0001F4A0'
FROWN: str = '\U0001F641'
WARNING: str = '\U0001F6AB'


def main() -> None:
    """Main Function."""
    global points
    points = 0
    greet()
    print(f"Welcome {player}, please select an option.")
    print()
    intro_menu()
    

def intro_menu() -> None:
    """Menu for first run through."""
    print(f"Total Points: {STAR} {points}")
    print()
    print(f"{GREEN_SQUARE} Easy - Type A.")
    print(f"{YELLOW_SQUARE} Normal - Type B.")
    print(f"{RED_SQUARE} Hard - Type C.")
    print()
    choice: str = input(f"{UP} Choose from the options above {UP} ")
    if choice == str("A"):
        number_guesser_easy()
    if choice == str("B"):
        number_guesser_normal()
    if choice == str("C"):
        number_guesser_hard()


def menu() -> None:
    """Menu for Loop."""
    print(f"Total Points: {STAR} {points}")
    print()
    print(f"{GREEN_SQUARE} Easy - Type A.")
    print(f"{YELLOW_SQUARE} Normal - Type B.")
    print(f"{RED_SQUARE} Hard - Type C.")
    print()
    print(f"{BLUE_CIRCLE} Spin the Point Wheel ({WARNING} Warning High Risk!) - Type D.")
    print()
    print(f"{EXIT} Exit - Type E.")
    print()
    choice: str = input(f"{UP} Choose from the options above {UP} ")
    if choice == str("A"):
        number_guesser_easy()
    if choice == str("B"):
        number_guesser_normal()
    if choice == str("C"):
        number_guesser_hard()
    if choice == str("D"):
        point_wheel(points)
    if choice == ("E"):
        exit()
    

def greet() -> None:
    """Greet the player."""
    print()
    print(f"{BLUE_DIAMOND} NUMBER GUESSER {BLUE_DIAMOND}")
    print()
    print("Welcome to Number Guesser! Get ready to guess the number correctly to earn points towards your score!")
    print()
    global player
    player = input("What is your name player? ")
    print()


def number_guesser_easy() -> None:
    """Easy Mode."""
    print()
    print(f"{GREEN_SQUARE} {player}, you've selected the Easy Difficulty")
    from random import randint
    number: int = randint(0, 5)
    global points
    print()

    guess = input("I'm thinking of a number from 0 to 5, what is your guess? ")
    print()
    i: int = 0

    if int(guess) == number:
        print("That was correct!")
        i = i + 1
        print("You guessed it on you first try!")
    else:
        i = 1
        while int(guess) != number:
            print("Nope that wasn't it")
            guess = input("Guess again. ")
            i = i + 1
        print("That was correct.")
        print(f"It took you {i} tries.")
    
    if i == 1:
        points = points + 7
        print(f"You have been awarded {STAR} 7 points!")
    if i > 1 and i <= 3:
        points = points + 5
        print(f"You have been awarded {STAR} 5 points!")
    if i > 3:
        points = points + 3
        print(f"You have been awarded {STAR} 3 points!")
    print()
    print(f"Total Points: {STAR} {points}")
    enter: str = input("Press Enter to Continue")
    print(enter)
    print("Would you like to play again? Select an option to continue, or exit.")
    menu()


def number_guesser_normal() -> None:
    """Normal Mode."""
    print()
    print(f"{YELLOW_SQUARE} {player}, you've selected the Normal Difficulty")
    from random import randint
    number: int = randint(0, 10)
    global points
    print(number)

    guess: str = input("I'm thinking of a number from 0 to 10, what is your guess? ")
    print()
    i: int = 0

    if int(guess) == number:
        print("That was correct!")
        i = i + 1
        print("You guessed it on you first try!")
    else:
        i = 1
        while int(guess) != number:
            print("Nope that wasn't it")
            guess = input("Guess again. ")
            i = i + 1
        print("That was correct.")
        print(f"It took you {i} tries.")
    
    if i == 1:
        points = points + 10
        print(f"You have been awarded {STAR} 10 points!")
    if i > 1 and i <= 5:
        points = points + 7
        print(f"You have been awarded {STAR} 7 points!")
    if i > 6:
        points = points + 5
        print(f"You have been awarded {STAR} 5 points!")

    print()
    print(f"Total Points: {STAR} {points}")
    enter: str = input("Press Enter to Continue")
    print(enter)
    print("Would you like to play again? Select an option to continue, or exit.")
    menu()


def number_guesser_hard() -> None:
    """Hard Mode."""
    print()
    print(f"{RED_SQUARE} {player}, you've selected the Hard Difficulty")
    from random import randint
    number: int = randint(0, 15)
    global points
    print()

    guess: str = input("I'm thinking of a number from 0 to 15, what is your guess? ")
    print()
    i: int = 0

    if int(guess) == number:
        print("That was correct!")
        i = i + 1
        print("You guessed it on you first try!")
    else:
        i = 1
        while int(guess) != number:
            print("Nope that wasn't it")
            guess = input("Guess again. ")
            i = i + 1
        print("That was correct.")
        print(f"It took you {i} tries.")

    if i == 1:
        points = points + 15
        print(f"You have been awarded {STAR} 15 points!")
    if i > 1 and i <= 7:
        points = points + 10
        print(f"You have been awarded {STAR} 10 points!")
    if i > 7:
        points = points + 7
        print(f"You have been awarded {STAR} 7 points!")

    print()
    print(f"Total Points: {STAR} {points}")
    enter: str = input("Press Enter to Continue")
    print(enter)
    print("Would you like to play again? Select an option to continue, or exit.")
    menu()


def point_wheel(point: int) -> int:
    """Spin the Point Wheel."""
    print()
    print(f"{BLUE_CIRCLE} You have selected to Spin the Point Wheel! {BLUE_CIRCLE}")
    enter = input("Press Enter to spin the Wheel!")
    print(enter)
    from random import randint
    global points
    outcome: int = randint(1, 3)
    if outcome == 1:
        points = points * 2
        print(f"You have landed on {SMILE} 2x points! {STAR} Your points have been doubled!")
        print(f"Total Points: {STAR} {points}")
    if outcome == 2:
        points = points - 2
        print(f"You have landed on {FROWN} -2 points. {STAR} 2 points have been deducted from your total.")
        print(f"Total Points: {STAR} {points}")
    if outcome == 3:
        points = points - 1
        print(f"You have landed on {FROWN} -1 point. {STAR} 1 point has been deducted from your total.")
        print(f"Total Points: {STAR} {points}")
    enter = input("Press Enter to Continue")
    print(enter)
    print("Would you like to play again? Select an option to continue, or exit.")
    menu()
    return points
     

def exit() -> None:
    """Exit the Game."""
    print()
    print(f"Thanks for playing {player}! Have a great day!")


if __name__ == "__main__":
    main()