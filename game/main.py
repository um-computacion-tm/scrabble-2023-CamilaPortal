from game.scrabble import ScrabbleGame
# def get_player_count():
#     while True:
#         try:
#             player_count= int(input("cantidad de jugadores: "))
#             if player_count <=1 or player_count > 4:
#                 break
#         except Exception as e:
#             print("Ingrese un numero entre 2 y 4")

#             return player_count
# def show_player(player_index, player):
#     print(f"player #{player_index}:{player.tiles}")

def main():
    # players_count = get_player_count()
    # game = ScrabbleGame(players_count)
    # while game.is_playing():
    #     show_board(game.get_board())
        # show_player(game.current_player, game.get_current_player())
        # word, coords, orientation = get_inpunts()
        # try:
        #     change = get_change_input()
        #     if change:
        #         letters= get_change_input()
        #         game.change(letters)
        #     else:
        #         word, coords, orientation = get_inputs()



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
