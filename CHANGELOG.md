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