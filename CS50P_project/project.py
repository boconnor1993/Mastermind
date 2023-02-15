import random, logging


def main():
    # Set logging level
    logging.basicConfig(level=logging.INFO)
    # Introduce game and rules
    print("===============================================================================================")
    print("|| Welcome to CS50 Mastermind! In this game, you will guess a random combination of colours. ||")
    print("||            To do so, enter the first letter of the colour and press space.                ||")
    print("||                  You will have 8 attempts to guess correctly.                             ||")
    print("||                       COLOURS TO GUESS: R, G, B, Y, W, P                                  ||")
    print("===============================================================================================")
    # Ask for difficulty and set combo accordingly
    colours = ["R","G","B","Y","W","P"]
    combo = secret_combo(colours)
    # Run through guesses
    for i in range(1,9):
        checker = True
        while checker:
            guess = input(f"Attempt #{i}: ").upper().split(" ")
            checker = validate_guess(guess, combo, colours)
        correct_pos, incorrect_pos = check_combo(guess, combo)
        print(f"Correct positions: {correct_pos}, Incorrect positions: {incorrect_pos}")
        if correct_pos == len(combo):
            print(f"Congratulations! You cracked the code in {i} attempts!")
            break
    else:
        print("Unlucky! You weren't able to guess the combination. The code was:", *combo, "!")


def secret_combo(colours):
    # Set opening variables
    combo = []
    difficulty_options = [1,2,3]
    # Run a loop until a valid difficulty is input
    while True:
        difficulty = input("Choose a difficulty from 1 to 3: ")
        if int(difficulty) not in difficulty_options:
            print("Please enter a difficulty between 1 and 3.")
            continue
        else:
            break
    combo_len = 2 * int(difficulty)
    print(f"You have chosen difficulty {difficulty}. The code to crack is {combo_len} colours long.")
    # Based on difficulty, create a combo
    for _ in range(int(combo_len)):
        combo.append(random.choice(colours))
    logging.debug(combo)
    logging.debug(f"Combo length is {len(combo)}")
    return combo


def validate_guess(guess, combo, colours):
    # Take input and validate on combo length and check against colours
    combo_len = len(combo)
    if len(guess) != combo_len:
        print(f"Invalid response: You must guess {combo_len} colours! Try again")
        return True
    for colour in guess:
        if colour not in colours:
            print(f"Invalid response: {colour} is not a valid colour! Try again")
            return True
    else:
        return False
        

def check_combo(guess, combo):
    # Initialise variables to be used
    colour_counter = {}
    correct_pos = 0
    incorrect_pos = 0
    
    # Check set colour_counter with initial count
    for colour in combo:
        if colour not in colour_counter:
            colour_counter[colour] = 0
        colour_counter[colour] += 1
    logging.debug(colour_counter)
    
    # Run through guess and combo to iterate through correct_pos
    for guess_colour, combo_colour in zip(guess, combo):
        if guess_colour == combo_colour:
            correct_pos += 1
            colour_counter[guess_colour] -= 1
            logging.debug(colour_counter)
    
    # Run through guess and combo to iterate through incorrect_pos
    for guess_colour, combo_colour in zip(guess, combo):
        if guess_colour in colour_counter and colour_counter[guess_colour] > 0:
            incorrect_pos += 1
            colour_counter[guess_colour] -= 1
            logging.debug(colour_counter)
            
    return correct_pos, incorrect_pos


if __name__ == "__main__":
    main()