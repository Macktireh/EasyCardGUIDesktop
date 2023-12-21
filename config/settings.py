from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

IMAGES_DIR = BASE_DIR / "assets" / "images"


class AssetsImages:
    ICON = "icon.ico"
    LOGO = "logo.png"
    DASHBOARD_DARK = "dashboard-white.png"
    DASHBOARD_LIGHT = "dashboard-black.png"
    NEW_DARK = "new-white.png"
    NEW_LIGHT = "new-black.png"
    DATA_DARK = "data-white.png"
    DATA_LIGHT = "data-black.png"
    SETTING_DARK = "setting-white.png"
    SETTING_LIGHT = "setting-black.png"
    EXIT_DARK = "exit-white.png"
    EXIT_LIGHT = "exit-black.png"


class Color:
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    GRAY = "#CCCCCC"
    RED = "#c60101"
    TEXT = ("#000000", "#ffffff")
    BG_CONTENT = ("#e0e0ff", "#2b2b31")
    BG_NAVIGATION = ("#d2d2fe", "#333338")
    BG_BUTTON_NAVIGATION = "transparent"
    BG_ACTIVE_BUTTON_NAVIGATION = ("#5d5d98", "#545473")
    BG_HOVER_BUTTON_NAVIGATION = ("#6e6eaa", "#65658b")
    BG_CARD = ("#ccccff", "#31313a")
    LIST_BG_PIE = (
        ["#6a6aa9", "#7a7ab8", "#5d5d98", "#5c5c8a", "#595978"],
        ["#4b4b72", "#404068", "#545473", "#64647d", "#777783"],
    )


class ScreenName:
    DASHBOARD = "dashboard"
    DASHBOARD_TITLE = "Dashboard"
    NEW = "new"
    NEW_TITLE = "New Card"
    DATA = "data"
    DATA_TITLE = "Data"
    SETTING = "setting"
    SETTING_TITLE = "Setting"


LIST_SCREEN = [
    ScreenName.DASHBOARD,
    ScreenName.NEW,
    ScreenName.DATA,
    ScreenName.SETTING,
]
