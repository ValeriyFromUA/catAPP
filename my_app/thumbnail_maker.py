from typing import NoReturn

from PIL import Image


def resize_image(post_preview_image, size=(900, 900)) -> NoReturn:
    img = Image.open(post_preview_image.path)
    img.thumbnail(size)
    img.save(post_preview_image.path)
