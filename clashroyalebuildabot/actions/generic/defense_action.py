from clashroyalebuildabot.actions.generic.action import Action


class DefenseAction(Action):
    """
    If there are enemies on our side,
    play the card in one of the defensive positions.
    Chooses side based on where enemy troops are stronger.
    """

    # Configurable defensive positions
    DEFENSE_POSITIONS = {
        (7, 9),  # left defensive tile
        (10, 9), # right defensive tile
        (8, 10), # optional center defense
    }

    def calculate_score(self, state):
        if (self.tile_x, self.tile_y) not in self.DEFENSE_POSITIONS:
            return [0]

        lhs = 0
        rhs = 0
        for det in state.enemies:
            if det.position.tile_y < 19 and det.position.tile_x <= 2:
                continue  # enemy not advanced enough

            if det.position.tile_x >= 9:
                rhs += 1
            else:
                lhs += 1

        if lhs == rhs == 0:
            return [0]

        # Avoid placing on the wrong lane
        if lhs >= rhs and self.tile_x >= 9:
            return [0]
        if rhs > lhs and self.tile_x <= 8:
            return [0]

        return [1]

