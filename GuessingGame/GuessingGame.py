import random

def display_heading():
    print("\n** Welcome to the Guessing Game! **\n")
    
def play_game(limit):
    random_number = random.randint(1, limit)
    print("I'm thinking of a number between 1 and {}. Can you guess what it is?".format(limit))
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < random_number:
                print("Too low, try again")
            elif guess > random_number:
                print("Too high, try again")
            else:
                print("Congrats! You guessed the number {} correctly!\n".format(random_number))
                break
        except ValueError:
            print("Please enter a valid number")
              
def main():
    while True:
        display_heading()
        try:
            limit = int(input("Enter the upper limit for the guessing range: "))
            
            if limit <=0:
                print("Please enter a number greater than 0.")
                continue
            
            play_game(limit)
            play_again = input("Do you want to play again? (y/n) ").strip().lower()
            if play_again != 'y':
                print("Goodbye")
                break
        except ValueError:
            print("please enter a valid number")
            
if __name__ == "__main__":
    main()
            
            