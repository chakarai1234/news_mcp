import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import httpx
from news_mcp.models import RequestTags

from news_mcp.models import ResponseModel


load_dotenv()

request_tags = RequestTags()


class NewsArticles:
    def __init__(self, url: str, timeout: int):
        self.url = url
        self.timeout = timeout
        self.heading_tag = None
        self.content_tag = None

    def fetch_article(self, recent: int = 5) -> list[ResponseModel]:
        if self.heading_tag is None and self.content_tag is None:
            raise ValueError("Set the self.heading_tag and self.content_tag to fetch thee data from the web")
        response_model: list[ResponseModel] = []
        try:
            resp = httpx.get(self.url, timeout=self.timeout, follow_redirects=True)
            resp.raise_for_status()
            content = resp.content
            root = ET.fromstring(content)
            if root.tag.endswith("rss"):
                channel = root.find("channel")
                for it in channel.findall("item"):
                    if len(response_model) == recent:
                        break
                    else:
                        resp_html = httpx.get(it.findtext(request_tags.link), timeout=self.timeout, follow_redirects=True)
                        bs = BeautifulSoup(resp_html.text, "html.parser")
                        heading = bs.select_one(self.heading_tag).get_text(strip=True)
                        if "For subscribers" in heading:
                            continue
                        title = it.findtext(request_tags.title)
                        link = it.findtext(request_tags.link)
                        date = it.findtext(request_tags.pubDate)
                        description = it.findtext(request_tags.description)
                        content = bs.select_one(self.content_tag).get_text(strip=True)
                        model = ResponseModel(title=title, link=link, date=date, description=description, content=content)
                        response_model.append(model)
            return response_model
        except httpx.HTTPStatusError:
            return [ResponseModel(title="", link="", date="", description="", content="")]
