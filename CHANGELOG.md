## [0.0.16] - 8-10-2023

## ADDED

- Method 'draw_board' for the creation of the game board

## [0.0.15] - 7-10-2023

## FIXED

- Modified 'has_letters' method to receive a word instead of list of tiles
- Exception handling implementation (WordOutOfBoard)

## ADDED

- Method 'is_playing' in ScrabbleGame class

## [0.0.15] - 4-10-2023

## ADDED

- Method 'put_word' responsible for placing a word on the game board based on the given word, location, and orientation.

## [0.0.14] - 1-10-2023

## ADDED

- Implementation of 'dictionary' to validate words

## [0.0.13] - 29-09-2023

## ADDED

- Method 'has_letters' to check if the player has the necessary tiles (with specific letters and counts) to form a word

## [0.0.12] - 23-09-2023

## FIXED

- Refactor the 'validate_word_place_board' method to pass CodeClimate's checks.

## [0.0.12] - 22-09-2023

## ADDED

- Method 'validate_word_place_board' working correctly

## [0.0.11] - 21-09-2023

## ATTEMPT

- Working on the method 'validate_word_place_board'; it validates whether the word crosses with a word already placed but currently does not check if the word is in the middle

# [0.0.11] - 19-09-2023

## ATTEMPT

- Working on the method "validate_word_place_board" to validate if, in a non-empty board, the word crosses with a letter already placed.

## [0.0.11] - 18-09-2023

## ADDED

- Code added to "validate_word_place_board" to check if the word is vertical and its position is in the middle of the board

## [0.0.11] - 15-09-2023

## ADDED

- Creation of the method "validate_word_place_board" to check if the word is horizontal and its position is in the middle of the board

## [0.0.10] - 14-09-2023

## ADDED

- Creation of the method "is_empty" to check if the board is empty or not

## [0.0.10] - 13-09-2023

## FIXED

- Cognitive Complexity in "validate_word_inside_board"

## [0.0.10] - 11-09-2023

## ADDED

- Creation of the method "validate_word_inside_board" to verify if a word fits on the board according to the given orientation and location.

- Exception to check that the orientation is only V or H.

## [0.0.9] - 09-09-2023

## ADDED
 
 - Creation of main.py that contains the logic for the user to start playing.

## [0.0.9] - 08-09-2023

## ADDED
 
 - Creation of the method "next_turn" in the class Scrabble

## [0.0.8] - 07-09-2023

## ADDED
 
 - Implementation of the active or inactive state of cells for point calculation.

 ## FIXED

 - Replacement of the "calculate_word_value" function by a method

## [0.0.7] - 01-09-2023

## ADDED
 
 - CodeClimate and CircleCI Implemented.

## [0.0.7] - 31-08-2023

## FIXED

- Replacement of the "calculate_word_value" method by a function

## [0.0.6] - 26-08-2023

## ADDED

- Method for word multipliers added to the Cell class

## [0.0.5] - 25-08-2023

## ADDED

- Methods to set multipliers added to Board class

## [0.0.4] - 23-08-2023

## ADDED

- Creation of the ScrabbleGame class

## [0.0.4] - 23-08-2023

## ADDED

- Creation of the Board class

## [0.0.4] - 23-08-2023

## ADDED

- Creation of the Cell class
- Creation of the add_letter and calculate_value methods

## [0.0.4] - 23-08-2023

## ADDED

- Creation of the Player class

## FIXED

- Renamed files: models and tests_scrabble to tiles and tests_tiles

## [0.0.3] - 21-08-2023

## ADDED

- Creation of the 'joker' method that checks if the current letter of the tile is a joker ("*"), and if it is, it changes the letter to the new one provided
- Creation of an exception to indicate that it's not a joker tile.
- Creation of tests case for the method and the exception

## [0.0.2] - 19-08-2023

## ADDED

- Addition of the missing tiles with their corresponding values
- Creation of exceptions:
            - NoHayFichas: if the bag of tiles is empty, the NoHayFichas exception is raised.
            - ImposibleCambiarMasDe7: impossible to exchange more than 7 tiles, since each player has 7 tiles.
            - BolsaLlena: if the limit of 100 tiles is reached, the BolsaLlena exception is raised, which indicates that the bag is full.
- Creation of tests case for all exceptions

## [0.0.1] - 19-08-2023

## ADDED

- Creation of the Tile class 
- Creation of the BagTiles class 
- Creation of the test case "test_tile" to verify whether the Tile class constructor correctly initializes the letter and value attributes of a tile object.
- creation of the test case "test_bag_tiles":
            - Verifies the number of tiles
            - Verifies if the random.shuffle function was called exactly once.
            - Verifies if the list of tiles in the bag was passed as an argument to the random.shuffle function.
- Creation of the test case "test_take", designed to verify the behavior of the take method, used to remove a certain number of tiles from the bag of tiles
- Creation of the test case "test_put", designed to verify the behavior of the put method, used to add tiles to the bag of tiles