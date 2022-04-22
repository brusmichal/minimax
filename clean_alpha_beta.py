def alpha_beta(position, depth, alpha, beta, max_player):
    if depth == 0 or position == 'terminal':
        return evaluate(position)
    if current_player is max_player:
        max_eval = -math.inf
        for child in children(position):
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for child in children(position):
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
