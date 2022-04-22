import c4_alfa_beta as ai
import math

from games_examples.two_player_games.player import Player
from games_examples.two_player_games.games.connect_four import ConnectFour, ConnectFourMove, ConnectFourState


def run(depth_1, depth_2, with_print, interactive):
    p1 = Player('a')
    p2 = Player('b')
    game = ConnectFour(first_player=p1, second_player=p2)
    while not game.is_finished():
        game_state = game.state
        a_points, a_move = ai.alpha_beta(game_state, depth_1, -math.inf, math.inf, True)
        if not interactive:
            b_points, b_move = ai.alpha_beta(game_state, depth_2, -math.inf, math.inf, False)

        game.make_move(a_move)
        if with_print:
            print(a_points, str(game))
        if interactive:
            b_move = ConnectFourMove(int(input("Podaj nr kolumny:")))
            game.make_move(b_move)
        if with_print:
            if interactive:
                print(str(game))
            else:
                print(b_points, str(game))
    if game.get_winner() == p1:
        if with_print:
            print("Wygrywa a!")
        return 'a'
    elif game.get_winner() == p2:
        if with_print:
            print("Wygrywa b!")
        return 'b'
    else:
        if with_print:
            print("Remis!")
        return 'r'


def make_statistics(depth_1, depth_2):
    runs_number = 30
    sum_a = 0
    sum_b = 0
    sum_r = 0
    for i in range(runs_number):
        winner = run(depth_1, depth_2, False, False)
        if winner == 'a':
            sum_a += 1
        elif winner == 'b':
            sum_b += 1
        else:
            sum_r += 1
    print(
        f"Wygrane a: {sum_a / runs_number * 100}, wygrane b:{sum_b / runs_number * 100}, remisy: {sum_r / runs_number * 100} w procentach przypadków")


#make_statistics(1, 3)
run(1, 1, True, True)
