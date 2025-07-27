from abc import ABC, abstractmethod

class BaseScraper(ABC):
    def __init__(self, company):
        self.company = company

    @abstractmethod
    def scrape_jobs(self):
        """Return a list of jobs with keys: title, location, url, posted_at (optional)"""
        pass
