import c4_alfa_beta as ai
import math

from games_examples.two_player_games.player import Player
from games_examples.two_player_games.games.connect_four import ConnectFour, ConnectFourMove, ConnectFourState


def run(depth_1, depth_2, with_print, interactive):
    p1 = Player('a')
    p2 = Player('b')
    game = ConnectFour(first_player=p1, second_player=p2)
    a_points = b_points = 0
    if with_print:
        print(str(game))
    while not game.is_finished():
        game_state = game.state
        a_points, a_move = ai.alpha_beta(game_state, depth_1, -math.inf, math.inf, True)
        if with_print:
            print(f"Wartość ruchu a: {a_points} \n")
        game.make_move(a_move)
        if with_print:
            print(str(game))
        if interactive:
            b_move = ConnectFourMove(int(input("Podaj nr kolumny:")))
        else:
            b_points, b_move = ai.alpha_beta(game_state, depth_2, -math.inf, math.inf, False)
            if with_print:
                print(f"Wartość ruchu b: {b_points} \n")
        game.make_move(b_move)
        if with_print:
            print(str(game))
    if game.get_winner() == p1:
        if with_print:
            print("\nWygrywa a!")
        return 'p1'
    elif game.get_winner() == p2:
        if with_print:
            print("\nWygrywa b!")
        return 'p2'
    else:
        if with_print:
            print("\nRemis!")
        return 'r'


def make_statistics(depth_1, depth_2):
    runs_number = 100
    sum_a = sum_b = sum_r = 0
    for i in range(runs_number):
        winner = run(depth_1, depth_2, False, False)
        if winner == 'p1':
            sum_a += 1
        elif winner == 'p2':
            sum_b += 1
        else:
            sum_r += 1
    print(
        f"Wygrane a: {sum_a}, wygrane b:{sum_b}, remisy: {sum_r}.")


make_statistics(1, 1)

# run(1, 5, True, False)
