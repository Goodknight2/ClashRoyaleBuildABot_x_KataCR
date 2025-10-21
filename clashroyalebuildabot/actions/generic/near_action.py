import math
import random

from clashroyalebuildabot.actions.generic.action import Action


class NearAction(Action):
    """
    Play the card in a random location close to enemy units
    """

    def calculate_score(self, state):
        score = [0.5] if state.numbers.elixir.number == 10 else [0]
        for det in state.enemies:
            if det.position.tile_x <= 2:
                continue
            # Choose a random location within radius 1.5 around the enemy
            radius = 1.5
            angle = random.uniform(0, 2 * math.pi)
            r = random.uniform(0, radius)
            offset_x = r * math.cos(angle)
            offset_y = r * math.sin(angle)
            self.tile_x = det.position.tile_x + offset_x
            self.tile_y = det.position.tile_y + offset_y

            distance = math.hypot(
                det.position.tile_x - self.tile_x,
                det.position.tile_y - self.tile_y,
            )
            if distance < radius:
                score = [1, +distance]
        return score
