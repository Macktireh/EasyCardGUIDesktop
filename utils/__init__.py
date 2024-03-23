from collections import defaultdict
from datetime import datetime, timedelta
from typing import List, Literal, Tuple

import darkdetect

from config.settings import Color
from models.types import CreditCardDictOut, RCParams


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


# data = [
#     {
#         "publicId": "0dbcf58321f240b2a7b385fbfc80b9df",
#         "code": "769253652678",
#         "cardType": "1000",
#         "isValid": True,
#         "createdAt": "2024-02-23T18:49:02.311646",
#         "updatedAt": "2024-02-28T02:48:10.311646",
#     },
#     {
#         "publicId": "7ed16939bca14bd5b642e62a272ebeac",
#         "code": "256788291246",
#         "cardType": "2000",
#         "isValid": False,
#         "createdAt": "2024-02-17T07:08:38.455943",
#         "updatedAt": "2024-03-02T05:57:47.455943",
#     },
# ]


def TimestampToDatetime(row: List) -> List:
    """
    Takes a list of strings and returns a list with 'createdAt', 'updatedAt' in the format 'YYYY-MM-DD HH:MM:SS'

    Args:
        row (List): A list of strings containing the data to be converted.

    Returns:
        List: A list of strings with 'createdAt', 'updatedAt' in the format 'YYYY-MM-DD HH:MM:SS'
    """
    createdAt = datetime.strptime(row[4], "%Y-%m-%dT%H:%M:%S.%f")
    updatedAt = datetime.strptime(row[5], "%Y-%m-%dT%H:%M:%S.%f")
    row[4] = datetime.strftime(createdAt, "%Y-%m-%d %H:%M:%S")
    row[5] = datetime.strftime(updatedAt, "%Y-%m-%d %H:%M:%S")
    return row


def dataToTable(data: CreditCardDictOut) -> Tuple[List[str], List[List[str | int | bool | None]]]:
    """
    Takes a data dict as argument and returns a tuple of columns: list[str], rows: list[list[str | int | None]].

    Args:
        data (dict): A dictionary containing the data to be converted.

    Returns:
        tuple: A tuple containing the columns and rows of the data.
    """
    columns = list(data[0].keys())
    rows = [TimestampToDatetime(list(row.values())) for row in data]
    return columns, rows


def getCardsCreatedWeekAgo(cards):
    cards_per_day = defaultdict(int)

    # Date actuelle
    current_date = datetime.now()
    duration = timedelta(days=25)

    # Parcourir chaque carte dans la liste
    for card in cards:
        creation_date = datetime.strptime(card["createdAt"], "%Y-%m-%dT%H:%M:%S.%f")

        # Vérifier si la carte a été créée dans les 7 derniers jours
        if current_date - creation_date <= duration:
            # Extraire la date uniquement sans l'heure
            creation_day = creation_date.strftime("%Y-%m-%d")
            # Incrémenter le compteur de cartes pour ce jour
            cards_per_day[creation_day] += 1
    
    # Trier le dictionnaire par date
    sorted_cards_per_day = dict(sorted(cards_per_day.items(), key=lambda x: x[0]))

    # Extraire les données pour le tracé
    return list(sorted_cards_per_day.keys()), list(sorted_cards_per_day.values())
