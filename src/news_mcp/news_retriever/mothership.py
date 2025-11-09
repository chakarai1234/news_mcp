import os
from news_mcp.news_retriever.news_retriever import NewsArticles


class MothershipNews(NewsArticles):
    def __init__(self, url, timeout):
        super().__init__(url, timeout)
        self.heading_tag = ".title"
        self.content_tag = ".content"


URL = os.getenv("MOTHERSHIP_URL") or "https://mothership.sg/feed/"
TIMEOUT = int(os.getenv("TIMEOUT"))
mothership_news = MothershipNews(url=URL, timeout=TIMEOUT)


def mothership(recent: int = 5):
    raise NotImplementedError()
    # response = mothership_news.fetch_article(recent=recent)
    # if response:
    #     return response


def main() -> None:
    raise NotImplementedError()


if __name__ == "__main__":
    main()
