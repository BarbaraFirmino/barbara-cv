""" image load"""
import numpy as np
from numpy.typing import NDArray
from PIL import Image


def load_image(path: str) -> NDArray[np.uint8]:
    """Load image from path.

    Args:
        path (str): Path to image.

    Returns:
        np.ndarray: Image as numpy array.
    """
    image = Image.open(path)
    image = image.convert("L")
    return np.asarray(image)


def save_image(np_array: NDArray[np.uint8], path: str) -> None:
    """Save image to path.

    Args:
        image (np.ndarray): Image as numpy array.
        path (str): Path to save image.
    """
    image = Image.fromarray(np_array)
    image.save(path)
