import os
from news_mcp.news_retriever.news_retriever import NewsArticles


class CNANews(NewsArticles):
    def __init__(self, url, timeout):
        super().__init__(url, timeout)
        self.heading_tag = ".h1"
        self.content_tag = ".block-field-blocknodearticlefield-content"


URL = os.getenv("CNA_URL")
TIMEOUT = int(os.getenv("TIMEOUT"))
cna_times_news = CNANews(url=URL, timeout=TIMEOUT)


def cna(top: int = 5):
    response = cna_times_news.fetch_article(top=top)
    if response:
        return response


def main() -> None:
    cna_times_news = cna(top=5)
    if cna_times_news:
        print(cna_times_news[0])


if __name__ == "__main__":
    main()
