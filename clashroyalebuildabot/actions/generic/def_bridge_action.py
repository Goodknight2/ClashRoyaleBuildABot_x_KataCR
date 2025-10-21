from clashroyalebuildabot.actions.generic.action import Action


class DefBridgeAction(Action):

    def calculate_score(self, state):
        if (self.tile_x, self.tile_y) not in {(5, 9), (12, 9),(7, 9), (10, 9)}:
            return [0]
        left_hp = state.numbers.left_ally_princess_hp.number
        right_hp = state.numbers.right_ally_princess_hp.number
        lhs = 0
        rhs = 0
        for det in state.enemies:
            if det.position.tile_y < 16 and det.position.tile_x <= 2:
                continue

            if det.position.tile_x >= 9:
                rhs += 1
            else:
                lhs += 1
            if left_hp > right_hp :
                rhs += 0.5
            else:    
                lhs += 0.5
            if left_hp == 0:
                lhs = 0     
            if right_hp == 0:
                rhs = 0  
        if lhs == rhs == 0:
            return [0]

        if lhs >= rhs and self.tile_x == 9:
            return [0]

        return [1]

