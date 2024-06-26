from typing import Sequence, Tuple
import cv2
import numpy as np
from capra_opi.image_processors.ImageProcessor import ImageProcessor


class ShapePostProcessor(ImageProcessor):
    def __init__(self):
        super().__init__()
    
    def __call__(self, img:cv2.Mat, rects:np.ndarray, valid:np.ndarray, cnts:Sequence[cv2.Mat]) -> Tuple[np.ndarray,np.ndarray,np.ndarray,np.ndarray, Sequence[cv2.Mat]]:
        """

        Args:
            img (cv2.Mat): 
            rects (np.ndarray[np.float_]): 
            valid (np.ndarray[np.bool_]): 
            cnts (Sequence[cv2.Mat]): 

        Returns:
            Tuple[np.ndarray[np.bool_],np.ndarray[np.float_],np.ndarray[np.float_],np.ndarray[np.float_], Sequence[cv2.Mat]]: 
        """
        pass