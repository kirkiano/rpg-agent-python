from uuid import uuid4

from scraper import html_scraper


@html_scraper('https://junkscience.com')
def scrape_junkscience(soup):
    tags = soup.find_all('h2', {'class': 'entry-title'})
    return [dict(id=uuid4(), title=t.text) for t in tags]


SCRAPERS = [scrape_junkscience]
