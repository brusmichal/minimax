import numpy as np

import c4_alfa_beta as ai
import math

from games_examples.two_player_games.player import Player
from games_examples.two_player_games.games.connect_four import ConnectFour, ConnectFourMove, ConnectFourState


def run(depth_1, depth_2, with_print, interactive):
    p1 = Player('a')
    p2 = Player('b')
    game = ConnectFour(first_player=p1, second_player=p2)

    if with_print:
        print(str(game))
    while not game.is_finished():
        game_state = game.state
        if interactive:
            a_points, a_move = ai.alpha_beta(game_state, depth_1, -math.inf, math.inf, True)
            game.make_move(a_move)
            print(f"Wartość ruchu a: {a_points} \n")
            print(str(game))
            b_move = ConnectFourMove(int(input("Podaj nr kolumny:")))
            game.make_move(b_move)
            print(str(game))

        else:
            a_points, a_move = ai.alpha_beta(game_state, depth_1, -math.inf, math.inf, True)
            b_points, b_move = ai.alpha_beta(game_state, depth_2, -math.inf, math.inf, False)
            if with_print:
                game.make_move(a_move)
                print(f"Wartość ruchu a: {a_points} \n")
                print(str(game))
                game.make_move(b_move)
                print(f"Wartość ruchu b: {b_points} \n")
                print(str(game))
            else:
                game.make_move(a_move)
                game.make_move(b_move)

    winner = game.get_winner()
    if winner == p1:
        if with_print:
            print("\nWygrywa a!")
        return 'p1'
    elif winner == p2:
        if with_print:
            print("\nWygrywa b!")
        return 'p2'
    else:
        if with_print:
            print("\nRemis!")
        return 'r'


def make_statistics(depth_1, depth_2, to_print):
    runs_number = 30
    sum_a = sum_b = sum_r = 0
    for i in range(runs_number):
        winner = run(depth_1, depth_2, False, False)
        if winner == 'p1':
            sum_a += 1
        elif winner == 'p2':
            sum_b += 1
        else:
            sum_r += 1
    a_pct = round(100 * sum_a / runs_number)
    b_pct = round(100 * sum_b / runs_number)
    r_pct = round(100 * sum_r / runs_number)
    if to_print:
        print(
            f"Wygrane a: {a_pct}%, wygrane b: {b_pct}%, remisy: {r_pct}%.")
    return a_pct, b_pct, r_pct


make_statistics(3, 1, True)

# run(2, 1, True, False)

