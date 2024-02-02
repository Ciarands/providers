import httpx
from ..utils import source
from ..utils.scraper import BasicScraper
from ..extractors.vidplay import VidplayScraper
from ..extractors.filemoon import FilemoonScraper

class VidsrcTo(BasicScraper):
    pass

__metadata__ = {
    "rank": 0,
    "_type": source.STANDARD,
    "_class": VidsrcTo,
    "extractors": [VidplayScraper, FilemoonScraper]
}
