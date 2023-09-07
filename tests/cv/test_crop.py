"""Test Crop."""

import numpy as np
import pytest
from numpy.typing import NDArray

from barbara_cv.cv.operations import crop


def test_crop_with_fake_image(fake_image: NDArray[np.uint8]) -> None:
    """Test crop with fake image."""
    res = crop(fake_image, 0, 0, 2, 2)

    expected = np.array([[1, 2], [4, 5]])
    assert np.allclose(res, expected)


def test_crop_all_image(fake_image: NDArray[np.uint8]) -> None:
    """Test bright all image."""
    height, width = fake_image.shape
    res = crop(fake_image, 0, 0, height, width)

    assert np.allclose(res, fake_image)


def test_crop_with_invalid_params(fake_image: NDArray[np.uint8]) -> None:
    """Test bright with invalid params."""
    with pytest.raises(ValueError):
        crop(fake_image, -1, 0, 2, 2)

    with pytest.raises(ValueError):
        crop(fake_image, 0, -1, 2, 2)

    with pytest.raises(ValueError):
        crop(fake_image, 0, 0, 10, 2)

    with pytest.raises(ValueError):
        crop(fake_image, 0, 0, 2, 10)
        crop(fake_image, 0, 0, 2, 10)
