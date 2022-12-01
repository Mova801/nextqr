from typing import Optional

from new.popup import popup
from new.popup import error_popup
from new.popup import news_popup

DEV_GITHUB: str = "https://github.com/Mova801"


def get_conf_error_popup() -> popup.Popup:
    return error_popup.ErrorPopup(
        win_title="NextQr",
        title="NextQrApp Error",
        link=DEV_GITHUB
    )


def get_news_popup(news: Optional[list[str]]) -> popup.Popup:
    return news_popup.NewsPopup(
        win_title="NextQr",
        title="NextQrApp News",
        news=news
    )
