import os
from news_mcp.news_retriever.news_retriever import NewsArticles


class StraitsTimesNews(NewsArticles):
    def __init__(self, url, timeout):
        super().__init__(url, timeout)
        self.heading_tag = ".headline-stack"
        self.content_tag = ".storyline-wrapper"


URL = os.getenv("STRAITS_TIMES_URL")
TIMEOUT = int(os.getenv("TIMEOUT"))
straits_times_news = StraitsTimesNews(url=URL, timeout=TIMEOUT)


def straits_times(top: int = 5):
    response = straits_times_news.fetch_article(top=top)
    if response:
        return response


def main() -> None:
    straits_times_news = straits_times(top=5)
    if straits_times_news:
        print(straits_times_news[0])


if __name__ == "__main__":
    main()
