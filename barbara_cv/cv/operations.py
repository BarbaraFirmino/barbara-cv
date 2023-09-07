"""Image operations."""
import numpy as np
from numpy.typing import NDArray


def bright(image: NDArray[np.uint8], value: int) -> NDArray[np.uint8]:
    """Change image brightness.

    Args:
        image (np.ndarray): Image as numpy array.
        value (int): Value to change brightness.

    Returns:
        np.ndarray: Image as numpy array.
    """
    return np.clip(image.astype(np.int16) + value, 0, 255).astype(np.uint8)


def crop(image: NDArray[np.uint8], top: int, left: int, bottom: int, right: int) -> NDArray[np.uint8]:
    """Crop an image

    Args:
        image (NDArray[np.uint8]): 2D numpy array
        top (int): y0
        left (int): x0
        bottom (int): y1
        right (int): x1

    Returns:
        NDArray[np.uint8]: image cropped by params.
    """
    if top < 0 or left < 0 or bottom > image.shape[0] or right > image.shape[1]:
        raise ValueError("Invalid crop parameters")

    return image[top:bottom, left:right]
