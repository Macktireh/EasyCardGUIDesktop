import os
from collections import namedtuple
from typing import Literal

from customtkinter import CTkImage
from PIL import Image as PILImage

from config.settings import IMAGES_DIR

imagesTupple = namedtuple("images", ["light", "dark"])
imgs = imagesTupple(
    light="dashboard-white.png",
    dark="dashboard-black.png",
)


class Image(CTkImage):
    status: Literal["ok", "fail"]

    def __init__(self, image: imagesTupple | str | None = None, size: tuple = (25, 25)) -> None:
        if image and isinstance(image, imagesTupple):
            lightImg = PILImage.open(os.path.join(IMAGES_DIR, image.light))
            darkImg = PILImage.open(os.path.join(IMAGES_DIR, image.dark))
            self.image = super().__init__(light_image=lightImg, dark_image=darkImg, size=size)
            self.status = "ok"
        elif image and isinstance(image, str):
            self.image = super().__init__(PILImage.open(os.path.join(IMAGES_DIR, image)), size=size)
            self.status = "ok"
        else:
            self.status = "fail"
