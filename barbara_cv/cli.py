import typer
from typing_extensions import Annotated

from barbara_cv.cv.operations import bright, crop
from barbara_cv.io.image import load_image, save_image

app = typer.Typer()


@app.command(name="bright")
def bright_cli(image_path: str, value: int, output_path: Annotated[str, typer.Option()]):
    """Change image brightness.

    Args:
        image_path (str): Path to image.
        value (int): Value to change brightness.
        output_path (str): Path to save image.
    """
    image = load_image(image_path)
    res = bright(image, value)
    save_image(res, output_path)


@app.command(name="crop")
def crop_cli(image_path: str, top: int, left: int, bottom: int, right: int, output_path: str):
    """Crop image.

    Args:
        image_path (str): Path to image.
        top (int): Top border.
        left (int): Left border.
        bottom (int): Bottom border.
        right (int): Right border.
        output_path (str): Path to save image.
    """
    image = load_image(image_path)
    res = crop(image, top, left, bottom, right)
    save_image(res, output_path)
