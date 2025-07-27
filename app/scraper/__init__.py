from .brainstation import BrainStationScraper

def get_scraper(company):
    name = company.name.lower()
    if 'brain station 23' in name:
        return BrainStationScraper(company)
    return None
