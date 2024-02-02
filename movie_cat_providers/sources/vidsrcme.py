import httpx
from ..utils import source
from ..utils.scraper import BasicScraper
from ..extractors.vidsrcpro import VidsrcProScraper
from ..extractors.superembed import SuperembedScraper

class VidsrcMe(BasicScraper):
    pass

__metadata__ = {
    "rank": 0,
    "_type": source.STANDARD,
    "_class": VidsrcMe,
    "extractors": [VidsrcProScraper, SuperembedScraper]
}
