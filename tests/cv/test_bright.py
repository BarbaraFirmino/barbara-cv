"""Test bright."""
import numpy as np
import pytest
from numpy.typing import NDArray

from barbara_cv.cv.operations import bright

im_test = np.array([[1, 2], [3, 4]])


@pytest.mark.parametrize(
    "image, value, expected",
    [
        (im_test, 1, np.array([[2, 3], [4, 5]])),
        (im_test, 100, np.array([[101, 102], [103, 104]])),
        (im_test, 300, np.array([[255, 255], [255, 255]])),
        (im_test, -100, np.array([[0, 0], [0, 0]])),
        (im_test, -1, np.array([[0, 1], [2, 3]])),
    ],
)
def test_bright(image: NDArray[np.uint8], value: int, expected: NDArray[np.uint8]) -> None:
    """Test bright."""
    result = bright(image, value)
    assert np.array_equal(result, expected)


def test_bright_with_fake_image(fake_image: NDArray[np.uint8]) -> None:
    """Test bright with fake image."""
    result = bright(fake_image, 250)

    assert result.dtype == np.uint8
    assert result.min() == 251
    assert result.max() == 255
    assert result.shape == fake_image.shape
