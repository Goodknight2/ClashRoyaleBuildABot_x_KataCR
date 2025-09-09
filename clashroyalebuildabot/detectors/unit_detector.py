import os

import numpy as np

from clashroyalebuildabot.constants import DETECTOR_UNITS
from clashroyalebuildabot.constants import DISPLAY_HEIGHT
from clashroyalebuildabot.constants import DISPLAY_WIDTH
from clashroyalebuildabot.constants import MODELS_DIR
from clashroyalebuildabot.constants import SCREENSHOT_HEIGHT
from clashroyalebuildabot.constants import SCREENSHOT_WIDTH
from clashroyalebuildabot.constants import TILE_HEIGHT
from clashroyalebuildabot.constants import TILE_INIT_X
from clashroyalebuildabot.constants import TILE_INIT_Y
from clashroyalebuildabot.constants import TILE_WIDTH
from clashroyalebuildabot.namespaces.units import Position
from clashroyalebuildabot.namespaces.units import UnitDetection
from katacr_detection.katacr_detection.detect import ComboDetector
from katacr.constants.label_list import unit2idx, idx2unit


class UnitDetector:
    MIN_CONF = 0
    UNIT_Y_START = 0.05
    UNIT_Y_END = 0.80

    def __init__(self, detector):
        self.detector = detector
    @staticmethod
    def _get_tile_xy(bbox):
        x = (bbox[0] + bbox[2]) * DISPLAY_WIDTH / (2 * SCREENSHOT_WIDTH)
        y = bbox[3] * DISPLAY_HEIGHT / SCREENSHOT_HEIGHT
        tile_x = round(((x - TILE_INIT_X) / TILE_WIDTH) - 0.5)
        tile_y = round(
            ((DISPLAY_HEIGHT - TILE_INIT_Y - y) / TILE_HEIGHT) - 0.5
        )
        return tile_x, tile_y        

    def _post_process(self, pred, height, image):
        """
        pred[:, [1, 3]] *= self.UNIT_Y_END - self.UNIT_Y_START
        pred[:, [1, 3]] += self.UNIT_Y_START * height
        """

        allies = []
        enemies = []
        for p in pred:
            # x1, y1, x2, y2
            l, t, r, b, idx, conf, cls, side = p
            bbox = (round(l), round(t), round(r), round(b))
            tile_x, tile_y = self._get_tile_xy(bbox)
            position = Position(bbox, conf, tile_x, tile_y)
            unit = idx2unit[int(cls)]
            unit_detection = UnitDetection(unit, position)

            if side == 0:
                allies.append(unit_detection)
            else:
                enemies.append(unit_detection)

        return allies, enemies
    

    def run(self, image):
        height, width = image.height, image.width
        np_image = np.array(image)
        pred = self.detector.infer(np_image).boxes.data
        pred = pred[pred[:, 4] > self.MIN_CONF]
        allies, enemies = self._post_process(pred, height, image)
        return allies, enemies
