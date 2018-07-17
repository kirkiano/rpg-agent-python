from uuid import uuid4

from bs4 import BeautifulSoup

from web import get_web_page


async def scrape_theatlantic():
    html = await get_web_page('https://theatlantic.org/')
    soup = BeautifulSoup(html, 'html.parser')
    return [dict(id=uuid4(), title=t.text.strip())
            for t in soup.find_all('h2', {'class': 'o-hed'})]


SCRAPERS = [scrape_theatlantic]
