import os
from typing_extensions import List
from news_mcp.models import ResponseModel
from news_mcp.news_retriever.news_retriever import NewsArticles


class CNANews(NewsArticles):
    def __init__(self, url: str, timeout: int):
        super().__init__(url, timeout)
        self.heading_tag = ".h1"
        self.content_tag = ".block-field-blocknodearticlefield-content"


URL: str = os.getenv("CNA_URL")
TIMEOUT: int = int(os.getenv("TIMEOUT"))
cna_times_news: CNANews = CNANews(url=URL, timeout=TIMEOUT)


def cna(recent: int = 5):
    response: List[ResponseModel] = cna_times_news.fetch_article(recent=recent)
    if response:
        return response


def main() -> None:
    cna_times_news: List[ResponseModel] = cna(recent=5)
    if cna_times_news:
        print(cna_times_news[0])


if __name__ == "__main__":
    main()
