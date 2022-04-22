import math

import numpy as np


def evaluate(game_state):
    return game_state.get_heuristic()


def get_winner(game_state):
    return game_state.get_winner()


def current_player(game_state):
    return game_state.get_current_player()


def is_finished(game_state):
    return game_state.is_finished()


# def make_children(game_state):
#     possible_moves = game_state.get_moves()
#     possible_states = []
#     for move in possible_moves:
#         possible_states += [game_state.make_move(move)]
#     return possible_states, possible_moves


def alpha_beta(game_state, depth, alpha, beta, maximising_player):
    rng = np.random.default_rng()
    if depth == 0 or is_finished(game_state):
        if is_finished(game_state):
            winner = get_winner(game_state)
            if winner is current_player(game_state):
                return 10e6, None
            elif winner is not current_player(game_state):
                return -10e6, None
            else:
                return 0, None
        else:
            # return evaluate(game_state), None
            return 0, None
    if maximising_player:
        max_eval = -math.inf
        possible_moves = game_state.get_moves()
        rng.shuffle(possible_moves)
        best_move = rng.choice(possible_moves)
        for move in possible_moves:
            state = game_state.make_move(move)
            eval = alpha_beta(state, depth - 1, alpha, beta, False)[0]
            if eval > max_eval:
                max_eval = eval
                best_move = move
            elif max_eval == eval:
                best_move = rng.choice([best_move, move])
            else:
                best_move = rng.choice(possible_moves)
            # max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return max_eval, best_move
    else:
        min_eval = math.inf
        possible_moves = game_state.get_moves()
        rng.shuffle(possible_moves)
        best_move = rng.choice(possible_moves)
        for move in possible_moves:
            state = game_state.make_move(move)
            eval = alpha_beta(state, depth - 1, alpha, beta, True)[0]
            if eval < min_eval:
                min_eval = eval
                best_move = move
            elif min_eval == eval:
                best_move = rng.choice([best_move, move])
            else:
                best_move = rng.choice(possible_moves)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move
