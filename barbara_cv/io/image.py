import numpy as np
from PIL import Image

def load_image(path: str):
    """Load image from path.

    Args:
        path (str): Path to image.

    Returns:
        np.ndarray: Image as numpy array.
    """
    image = Image.open(path)
    image = image.convert('L')
    return np.asarray(image)

def save_image(image: np.ndarray, path: str):
    """Save image to path.

    Args:
        image (np.ndarray): Image as numpy array.
        path (str): Path to save image.
    """
    image = Image.fromarray(image)
    image.save(path)