def process_move(self, move):
    """Process the current move and check if it's a win."""
    # TODO: check whether the current move leads to a winning combo.
    # Do not return any values but set variables  self._has_winner
    # and self.winner_combo in case of winning combo.
    # Hint: you can scan pre-computed winning combos in self._winning_combos
    row, col = move.row, move.col
    self._current_moves[row][col] = move
    for combo in self._winning_combos:
        results = set(
            self._current_moves[n][m].label
            for n, m in combo
        )
        is_win = (len(results) == 1) and ("" not in results)
        if is_win:
            self._has_winner = True
            self.winner_combo = combo
            break

