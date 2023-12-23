from typing import Literal

import darkdetect

from config.settings import Color
from models.types import RCParams


def getSystemTheme() -> Literal["dark", "light"]:
    """
    Get the system theme.

    Returns:
        The system theme as a string. It can be either "dark" or "light".
    """
    return "dark" if darkdetect.theme() == "Dark" else "light"


def rcParams(theme: Literal["dark", "light"]) -> RCParams:
        """
        Generates the RCParams object for customizing the appearance of plots based on the current appearance mode.

        Args:
            theme (str): The name of the theme to be used. Can be either 'light' or 'dark'.
        
        Returns:
            RCParams: The RCParams object with the customized appearance settings.
        """
        axesFaceColor = Color.BG_CARD[1] if theme == "dark" else Color.BG_CARD[0]
        xTickColor = Color.WHITE if theme == "dark" else Color.BLACK
        yTickColor = Color.WHITE if theme == "dark" else Color.BLACK

        return RCParams(
            axesFaceColor=axesFaceColor,
            figureFaceColor=axesFaceColor,
            savefigFaceColor=axesFaceColor,
            axesEdgecolor=axesFaceColor,
            xTickColor=xTickColor,
            yTickColor=yTickColor,
        )
