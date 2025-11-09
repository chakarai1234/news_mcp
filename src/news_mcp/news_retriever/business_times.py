import os
from news_mcp.news_retriever.news_retriever import NewsArticles


class BusinessTimesNews(NewsArticles):
    def __init__(self, url: str, timeout: int):
        super().__init__(url, timeout)
        self.heading_tag = '[data-testid="article-title"]'
        self.content_tag = '[data-testid="article-body-container"]'


URL = os.getenv("BUSINESS_TIMES_URL")
TIMEOUT = int(os.getenv("TIMEOUT"))
business_times_news = BusinessTimesNews(url=URL, timeout=TIMEOUT)


def business_times(recent: int = 5):
    response = business_times_news.fetch_article(recent=recent)
    if response:
        return response


def main() -> None:
    business_times_news = business_times(recent=5)
    if business_times_news:
        print(business_times_news[0])


if __name__ == "__main__":
    main()
