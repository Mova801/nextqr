from typing import Optional

from new import popup

DEV_GITHUB: str = "https://github.com/Mova801"


def get_conf_error_popup() -> popup.popup.Popup:
    return popup.error_popup.ErrorPopup(
        win_title="NextQr",
        title="NextQrApp Error",
        link=DEV_GITHUB
    )


def get_news_popup(news: Optional[list[str]]) -> popup.popup.Popup:
    return popup.news_popup.NewsPopup(
        win_title="NextQr",
        title="NextQrApp News",
        news=news
    )
