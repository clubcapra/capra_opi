import cv2
import numpy as np
from capra_opi.lib.common import ORANGE
from .Contraster import Contraster


class MeanRGBOffset(Contraster):
    def __init__(self, color=ORANGE):
        super().__init__()
        self.color = color
        
    def __call__(self, img: cv2.Mat) -> cv2.Mat:
        dist = np.abs(img.astype(np.int16) - ORANGE)
        res = dist.mean(2).astype(np.uint8)
        self.debugImg(res)
        return res