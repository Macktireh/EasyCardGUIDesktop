from collections import namedtuple
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

IMAGES_DIR = BASE_DIR / "assets" / "images"

BASE_API_URL = "http://localhost:5000/api"

imagesTupple = namedtuple("images", ["light", "dark"])


class AssetsImages:
    ICON = "icon.ico"
    LOGO = "logo.png"
    CARD_CREDIT_DARK = "card-credit.jpg"
    CARD_CREDIT_LIGHT = "card-credit.jpg"
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
    DELETE_DARK = "delete.png"
    DELETE_LIGHT = "delete.png"
    DRAG_AND_DROP_DARK = "drag-and-drop-white.png"
    DRAG_AND_DROP_LIGHT = "drag-and-drop-black.png"
    EXTRACT_DARK = "extract.png"
    EXTRACT_LIGHT = "extract.png"
    SAVE_DARK = "save-white.png"
    SAVE_LIGHT = "save-black.png"
    EDIT_DARK = "edit-white.png"
    EDIT_LIGHT = "edit-black.png"
    CROSS_DARK = "cross-white.png"
    CROSS_LIGHT = "cross-black.png"
    ADD_DARK = "add-white.png"
    ADD_LIGHT = "add-black.png"
    MENU_DARK = "menu-white.png"
    MENU_LIGHT = "menu-black.png"
    API_DARK = "api-white.png"
    API_LIGHT = "api-black.png"
    GENERAL_DARK = "general-white.png"
    GENERAL_LIGHT = "general-black.png"
    HELP_DARK = "help-white.png"
    HELP_LIGHT = "help-black.png"
    THEME_DARK = "theme-white.png"
    THEME_LIGHT = "theme-black.png"
    PRIVACY_DARK = "privacy-white.png"
    PRIVACY_LIGHT = "privacy-black.png"
    NOTIFICATION_DARK = "notification-white.png"
    NOTIFICATION_LIGHT = "notification-black.png"
    KEY_DARK = "key-white.png"
    KEY_LIGHT = "key-black.png"
    EYE_DARK = "eye-white.png"
    EYE_LIGHT = "eye-black.png"
    EYE_CLOSED_DARK = "eye-closed-white.png"
    EYE_CLOSED_LIGHT = "eye-closed-black.png"
    RELOAD_DARK = "reload-white.png"
    RELOAD_LIGHT = "reload-black.png"
    INFO_DARK = "info-white.png"
    INFO_LIGHT = "info-black.png"
    LOADING_GIF = BASE_DIR / "assets" / "images" / "spin2.gif"


class Color:
    TRANSPARENT = "transparent"
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    GRAY = "#CCCCCC"
    RED = "#c60101"
    ORANGE = "#d97706"
    GREEN = "#017a01"
    BLUE = "#035fa1"
    TEXT = ("#000000", "#FFFFFF")
    TEXT_GRAY = ("#535050", "#9e9a9a")
    BG_CONTENT = ("#e0e0ff", "#2b2b31")
    BG_BUTON_DND = ("#d7d7fe", "#393941")
    BG_CONTENT_SECONDARY = ("#c2c2ff", "#393941")
    BG_NAVIGATION = ("#d2d2fe", "#333338")
    BG_BUTTON_NAVIGATION = "transparent"
    BG_ACTIVE_BUTTON_NAVIGATION = ("#5d5d98", "#545473")
    BG_HOVER_BUTTON_NAVIGATION = ("#6e6eaa", "#65658b")
    BG_CARD = ("#ccccff", "#31313a")
    LIST_BG_PIE = (
        ["#6a6aa9", "#7a7ab8", "#5d5d98", "#5c5c8a", "#595978"],
        ["#4b4b72", "#404068", "#545473", "#64647d", "#777783"],
    )
    BG_SPLASH = "#e0e0ff"
    BG_ALT_TREEVIEW = ("#ccccff", "#afafd5")


class ScreenName:
    LOGIN = "login"
    LOGIN_TITLE = "Login"
    DASHBOARD = "dashboard"
    DASHBOARD_TITLE = "Dashboard"
    NEW = "new"
    NEW_TITLE = "New Card"
    DATA = "data"
    DATA_TITLE = "Data"
    SETTING = "setting"
    SETTING_TITLE = "Setting"


LIST_SCREEN = [
    ScreenName.LOGIN,
    ScreenName.DASHBOARD,
    ScreenName.NEW,
    ScreenName.DATA,
    ScreenName.SETTING,
]

LIST_CARD_TYPES = [
    "500 FDJ",
    "1000 FDJ",
    "2000 FDJ",
    "5000 FDJ",
    "10000 FDJ",
]
