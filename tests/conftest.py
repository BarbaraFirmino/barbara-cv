import numpy as np
import pytest
from numpy.typing import NDArray


@pytest.fixture(scope="session")
def fake_image() -> NDArray[np.uint8]:
    return np.arange(1, 10).reshape(3, 3).astype(np.uint8)
