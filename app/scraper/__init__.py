from .brainstation import BrainStationScraper
from .therap import TherapScraper

def get_scraper(company):
    name = company.name.lower()
    if 'brain station 23' in name:
        return BrainStationScraper(company)
    elif 'therap' in name:
        return TherapScraper(company)
    return None
