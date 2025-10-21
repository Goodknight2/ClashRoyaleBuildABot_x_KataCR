from clashroyalebuildabot.actions.generic.action import Action


class BridgeAction(Action):
    """
    If you have 7 elixir,
    play this card at the bridge on the side of the weakest tower,
    but avoid bridge spam if enemies are already pushing that side.
    """

    def calculate_score(self, state):
        if (self.tile_x, self.tile_y) not in {(3, 15), (14, 15)}:
            return [0]

        if state.numbers.elixir.number < 4:
            return [0]

        left_hp = state.numbers.left_enemy_princess_hp.number
        right_hp = state.numbers.right_enemy_princess_hp.number

        # Count enemies per lane
        lhs = 0
        rhs = 0
        for det in state.enemies:
            if det.position.tile_y > 16:
                continue  # skip enemies not advanced enough

            if det.position.tile_x >= 9:
                rhs += 1
            else:
                lhs += 1

        if self.tile_x == 3:
            # Left bridge
            if lhs > 0:
                return [0]  # avoid if enemies are already pushing left
            score = [1, left_hp > 0, left_hp <= right_hp]
        else:
            # Right bridge (tile_x == 14)
            if rhs > 0:
                return [0]  # avoid if enemies are already pushing right
            score = [1, right_hp > 0, right_hp <= left_hp]

        return score
