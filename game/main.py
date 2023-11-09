from game.scrabble import ScrabbleGame, NoJoker
from game.board import Board, SoloVoHParaLaOrientacion
from game.cell import Cell
from game.player import Player

class Main:
    def get_player_count(self):
        while True:
            try:
                player_count= int(input("cantidad de jugadores (2-4): "))
                if player_count >= 2 and player_count <= 4:
                    break
            except Exception as e:
                print("Ingrese un numero entre 2 y 4")

        return player_count

    def show_board(self, board):
        print("   |  " + "  |  ".join(str(item) for item in range(10)) + "  | " + "  | ".join(str(item) for item in range(10, 15)) + " |")
        print("   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        for i, row in enumerate(board.grid):
            row_str = f"{i:2d} | " + " | ".join(repr(cell) for cell in row) + " |"
            print(row_str)
            print("   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")

            
    def show_player(self, player_index, player):
        print(f"Player #{player_index}:{player.tiles} score: {player.score}")

    def get_location(self):
        while True:
            try:
                location_x = int(input("Ingrese la posición de la fila: "))
                location_y = int(input("Ingrese la posición de la columna: "))
                location = location_x,location_y
                return location
            except Exception as e:
                print("Error: Ingrese numeros validos para la posicion.")

    def get_word(self):
        while True:
            try:
                word = input("Ingrese la palabra: ").upper()
                if word.isalpha():
                    return word
            except Exception as e:
                print("Error: Ingresa una palabra valida")
    
    def get_orientation(self):
        while True:
            try:
                orientation = input("Ingrese la orientación (H para horizontal, V para vertical): ").upper()
                if orientation == 'H' or orientation == 'V':
                    return orientation
                else:
                    raise SoloVoHParaLaOrientacion("Orientación invalida. Por favor, ingrese H para horizontal o V para vertical.")
            except Exception as e:
                print(f"Error: {e}")

    def play_word(self, game):
        try:
            word = self.get_word()
            location = self.get_location()
            orientation = self.get_orientation()
            rack = game.get_player_tiles()
            game.play(word, location, orientation, rack)
        except Exception as e:
            print(f'Error: {e}')

    def joker(self, game):
        if game.get_joker_index():
            try:
                letter = input("Ingrese la letra por la que desea cambiar el comodin: ")
                game.convert_joker_to_letter(letter)
            except Exception as e:
                print(f'Error: No tiene joker')

    def change(self, game):
        current_player = game.get_current_player()
        player_tiles = current_player.tiles
        game.bag_tiles.put(player_tiles)
        new_tiles = game.bag_tiles.take(7)
        current_player.tiles = new_tiles

    def pass_turn(self, game):
        game.next_turn()

    def end_game(self, game):
        winners = game.compare_score()
        if len(winners) == 1:
            winner = winners[0]
            print('-'*100)
            print(f"El ganador es: jugador #{game.players.index(winner)} con {winner.score} puntos")
        else:
            print('-'*100)
            print("¡Empate!")
            print("Los ganadores son:")
            for winner in winners:
                print(f"Jugador #{game.players.index(winner)} con {winner.score} puntos")
        exit()

    def play_scrabble(self):
        print("BIENVENIDO A SCRABBLE GAME")
        players_count = self.get_player_count()
        game = ScrabbleGame(players_count)
        menu_options = {
            '1': self.play_word,
            '2': self.pass_turn,
            '3': self.joker,
            '4': self.change,
            '5': self.end_game
        }
        while not game.finish_game():
            self.show_board(game.get_board())
            self.show_player(game.current_player, game.get_current_player())
            print("\nMenu:")
            print("1. Jugar palabra")
            print("2. Pasar turno")
            print("3. cambiar comodin")
            print("4. cambiar fichas")
            print("5. Terminar juego")
            print('-'*100)

            choice = input("Seleccione una opción: ")

            selected_option = menu_options.get(choice)
            if selected_option:
                selected_option(game)     
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        
        print('¡Juego finalizado!')
        self.end_game(game)


if __name__=="__main__":
    main = Main()
    main.play_scrabble()
