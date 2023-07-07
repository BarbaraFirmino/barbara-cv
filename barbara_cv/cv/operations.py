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
    return (image + value).astype(np.uint8)


def crop(image: NDArray[np.uint8], top: int, left: int, bottom: int, right: int) -> NDArray[np.uint8]:
    """Crop image.

    Args:
        image (np.ndarray): Image as numpy array.
        top (int): Top border.
        left (int): Left border.
        bottom (int): Bottom border.
        right (int): Right border.

    Returns:
        np.ndarray: Image as numpy array.
    """
    return image[top:bottom, left:right]
