import math

from clashroyalebuildabot import Cards
from clashroyalebuildabot.actions.generic.near_action import NearAction


class BabyDragonAction(NearAction):
    CARD = Cards.BABY_DRAGON

    def calculate_score(self, state):
        for det in state.enemies:
            if det.position.tile_x <= 2:
                continue
            distance = math.hypot(
                det.position.tile_x - self.tile_x,
                det.position.tile_y - self.tile_y,
            )
            if 5 < distance < 6:
                return [1]
            if distance < 5:
                return [0]
        return [0]
