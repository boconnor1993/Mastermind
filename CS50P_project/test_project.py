import pytest, mock
from project import secret_combo, validate_guess, check_combo

def test_secret_combo():
    # Test secret_combo() with difficulty = 1
    colours = ["R","G","B","Y","W","P"]
    with mock.patch('builtins.input', side_effect=[1]):
        combo = secret_combo(colours)
    assert len(combo) == 2
    assert all(color in colours for color in combo)

    # Test secret_combo() with difficulty = 2
    colours = ["R","G","B","Y","W","P"]
    with mock.patch('builtins.input', side_effect=[2]):
        combo = secret_combo(colours)
    assert len(combo) == 4
    assert all(color in colours for color in combo)

    # Test secret_combo() with difficulty = 3
    colours = ["R","G","B","Y","W","P"]
    with mock.patch('builtins.input', side_effect=[3]):
        combo = secret_combo(colours)
    assert len(combo) == 6
    assert all(color in colours for color in combo)


def test_validate_guess():
    # Test validate_guess() with a valid guess
    guess = ['R', 'G']
    combo = ['R', 'G']
    colours = ["R","G","B","Y","W","P"]
    assert validate_guess(guess, combo, colours) == False

    # Test validate_guess() with an invalid guess (wrong number of colours)
    guess = ['R']
    combo = ['R', 'G']
    colours = ["R","G","B","Y","W","P"]
    assert validate_guess(guess, combo, colours) == True
    
    # Test validate_guess() with an invalid guess (colour not in list)
    guess = ['M']
    combo = ['R', 'G']
    colours = ["R","G","B","Y","W","P"]
    assert validate_guess(guess, combo, colours) == True


def test_check_combo():
    # Test check_combo() with correct guess
    guess = ['R', 'G']
    combo = ['R', 'G']
    correct_pos, incorrect_pos = check_combo(guess, combo)
    assert correct_pos == 2
    assert incorrect_pos == 0

    # Test check_combo() with incorrect guess
    guess = ['R', 'B']
    combo = ['R', 'G']
    correct_pos, incorrect_pos = check_combo(guess, combo)
    assert correct_pos == 1
    assert incorrect_pos == 0