import os
from typing import Literal

from customtkinter import CTkImage
from PIL import Image as PILImage

from config.settings import IMAGES_DIR, imagesTupple


class Image(CTkImage):
    status: Literal["ok", "fail"]

    def __init__(self, image: imagesTupple | str | None = None, size: tuple = (25, 25), external: bool = False) -> None:
        self.status = "fail"
        if not image:
            return
        if isinstance(image, imagesTupple):
            if not external:
                light_path = os.path.join(IMAGES_DIR, image.light)
                dark_path = os.path.join(IMAGES_DIR, image.dark)
            else:
                light_path = image.light
                dark_path = image.dark
            lightImg = PILImage.open(light_path)
            darkImg = PILImage.open(dark_path)
            self.status = "ok"
        elif isinstance(image, str):
            image_path = image if external else os.path.join(IMAGES_DIR, image)
            lightImg = PILImage.open(image_path)
            darkImg = lightImg
            self.status = "ok"
        super().__init__(light_image=lightImg, dark_image=darkImg, size=size)
