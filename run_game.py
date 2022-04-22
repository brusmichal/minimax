import c4_alfa_beta as ai
import math

from games_examples.two_player_games.player import Player
from games_examples.two_player_games.games.connect_four import ConnectFour, ConnectFourMove, ConnectFourState

p1 = Player('a')
p2 = Player('b')
game = ConnectFour(first_player=p1, second_player=p2)

while not game.is_finished():
    game_state = game.state
    a_points, a_move = ai.alpha_beta(game_state, 1, -math.inf, math.inf, ['a', 'b'], True)
    b_points, b_move = ai.alpha_beta(game_state, 1, -math.inf, math.inf, ['a', 'b'], False)

    game.make_move(a_move)
    print(a_points, str(game))
    game.make_move(b_move)
    print(b_points, str(game))

if game.get_winner() == p1:
    print("Winner is a!")
else:
    print("Winner is b!")
