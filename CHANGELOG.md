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