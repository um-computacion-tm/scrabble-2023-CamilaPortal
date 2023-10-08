from game.scrabble import ScrabbleGame
# def show_player(player_index, player):
#     print(f"player #{player_index}:{player.tiles}")

def main():
    # players_count = get_player_count()
    # game = ScrabbleGame(players_count)
    # while game.is_playing():
    #     show_board()

    print("Bienvenido")
    while True:
        try:
            players_count = int(input("Ingrese cantidad de jugadores: "))
            if players_count <=1 or players_count > 4:
                raise ValueError
            break
        except ValueError:
            print("Ingrese un numero entre 2 y 4")

    scrabble_game = ScrabbleGame(players_count=players_count)
    print(f'Numero de jugadores: {len(scrabble_game.players)}' )
    scrabble_game.next_turn()
    print(f'Turno actual: jugador {scrabble_game.players.index(scrabble_game.current_player) + 1}')
    # word= input("Enter a word: ")
    # location_x = input("Enter x coordinate: ")
    # location_y = input("Enter y coordinate: ")
    # location = [location_x, location_y]
    # orientation = input("Enter orientation (V/H): ")

if __name__=="__main__":
    main()
