import os
from typing_extensions import List
from news_mcp.models import ResponseModel
from news_mcp.news_retriever.news_retriever import NewsArticles


class StraitsTimesNews(NewsArticles):
    def __init__(self, url: str, timeout: int):
        super().__init__(url, timeout)
        self.heading_tag: str = ".headline-stack"
        self.content_tag: str = ".storyline-wrapper"


URL: str = os.getenv("STRAITS_TIMES_URL")
TIMEOUT: int = int(os.getenv("TIMEOUT"))
straits_times_news: StraitsTimesNews = StraitsTimesNews(url=URL, timeout=TIMEOUT)


def straits_times(recent: int = 5):
    response: List[ResponseModel] = straits_times_news.fetch_article(recent=recent)
    if response:
        return response


def main() -> None:
    straits_times_news: List[ResponseModel] = straits_times(recent=5)
    if straits_times_news:
        print(straits_times_news[0])


if __name__ == "__main__":
    main()
