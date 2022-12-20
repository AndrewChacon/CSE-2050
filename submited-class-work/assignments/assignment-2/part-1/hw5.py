def solveable(p_idxs, k_idx):
    if len(p_idxs) == 0: return True
    else:
        moves = valid_moves(k_idx)
        for move in moves:
            if move in p_idxs:
                p_idxs.remove(move)
                if solveable(p_idxs, move): return True
                else: p_idxs.add(move)
        return False

def valid_moves(k_idx):
    v_moves = set()
    plays = 8
    for en in range(plays):
        for i in range(plays):
            if abs(k_idx[0] - en) == 2 and abs(k_idx[1] - i) == 1: v_moves.add((en,i))
            if abs(k_idx[0] - en) == 1 and abs(k_idx[1] - i) == 2: v_moves.add((en,i))
    return v_moves


