import random

class NoHayFichas(Exception):
    pass

class ImposibleCambiarMasDe7(Exception):
    pass

class BolsaLlena(Exception):
    pass

class NoEsUnJoker(Exception):
    pass

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

    def joker(self, new_letter):
        if self.letter == "*":
            self.letter = new_letter
        else:
            raise NoEsUnJoker(Exception)

class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile("A", 1), Tile("A", 1), Tile("A", 1), Tile("A", 1), Tile("A", 1), Tile("A", 1), Tile("A", 1), Tile("A", 1), Tile("A", 1), Tile("A", 1), Tile("A", 1), Tile("A", 1),
            Tile("E", 1), Tile("E", 1), Tile("E", 1), Tile("E", 1), Tile("E", 1), Tile("E", 1), Tile("E", 1), Tile("E", 1), Tile("E", 1), Tile("E", 1), Tile("E", 1), Tile("E", 1),
            Tile("O", 1), Tile("O", 1), Tile("O", 1), Tile("O", 1), Tile("O", 1), Tile("O", 1), Tile("O", 1), Tile("O", 1), Tile("O", 1),
            Tile("I", 1), Tile("I", 1), Tile("I", 1), Tile("I", 1), Tile("I", 1), Tile("I", 1),
            Tile("S", 1), Tile("S", 1), Tile("S", 1), Tile("S", 1), Tile("S", 1), Tile("S", 1),
            Tile("N", 1), Tile("N", 1), Tile("N", 1), Tile("N", 1), Tile("N", 1),
            Tile("L", 1), Tile("L", 1), Tile("L", 1), Tile("L", 1), 
            Tile("R", 1), Tile("R", 1), Tile("R", 1), Tile("R", 1), Tile("R", 1),
            Tile("U", 1), Tile("U", 1), Tile("U", 1), Tile("U", 1), Tile("U", 1),
            Tile("T", 1), Tile("T", 1), Tile("T", 1), Tile("T", 1),
            Tile("D", 2), Tile("D", 2), Tile("D", 2), Tile("D", 2), Tile("D", 2),
            Tile("G", 2), Tile("G", 2),
            Tile("C", 3), Tile("C", 3), Tile("C", 3), Tile("C", 3),
            Tile("B", 3), Tile("B", 3),
            Tile("M", 3), Tile("M", 3),
            Tile("P", 3), Tile("P", 3),
            Tile("H", 4), Tile("H", 4),
            Tile("F", 4),
            Tile("V", 4),
            Tile("Y", 4),
            Tile("CH", 5),
            Tile("Q", 5),
            Tile("J", 8),
            Tile("LL", 8),
            Tile("Ñ", 8),
            Tile("RR", 8),
            Tile("X", 8),
            Tile("Z", 10),
            Tile("*", 0),
            Tile("*", 0),
            
        ]
        random.shuffle(self.tiles)
    
    def take(self, count):
        tiles = []
        if len(self.tiles) == 0:
            raise NoHayFichas(Exception)
        else:
            for _ in range(count):
                tiles.append(self.tiles.pop())
            return tiles
        
    def put(self, tiles):
        if len(tiles) > 7:
            raise ImposibleCambiarMasDe7(Exception)
        elif len(self.tiles) == 100:
            raise BolsaLlena(Exception)
        else:
            self.tiles.extend(tiles)


