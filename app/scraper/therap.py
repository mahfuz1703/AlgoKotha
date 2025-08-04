import requests
from bs4 import BeautifulSoup
from .base import BaseScraper
import time

class TherapScraper(BaseScraper):
    def scrape_jobs(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
        }

        response = requests.get(self.company.careerPage, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        job_cards = soup.select(".js-careers-page-job-list-item")
        jobs_data = []

        for card in job_cards:
            relative_link = card.get("data-href")
            if not relative_link:
                continue

            job_link = self.company.careerPage + relative_link
            job_title_tag = card.select_one(".js-job-list-opening-name")
            job_title = job_title_tag.text.strip() if job_title_tag else "N/A"

            location_tag = card.select_one(".js-job-list-opening-loc")
            job_location = location_tag.get_text(separator=", ", strip=True) if location_tag else "N/A"

            department_tag = card.select_one(".col-md-4 .rb-text-4")
            job_department = department_tag.text.strip() if department_tag else "N/A"

            job_type_tag = card.select_one(".js-job-list-opening-meta")
            job_type = job_type_tag.get_text(separator=", ", strip=True) if job_type_tag else "N/A"

            jobs_data.append({
                "job_link": job_link,
                "job_title": job_title,
                "job_location": job_location,
                "job_department": job_department,
                "job_type": job_type,
                "job_apply_link": job_link,  # Trakstar jobs use same link to apply
                "job_vacancies": 0,  # Not available in the listing
                "job_salary": "N/A",
                "job_salary_type": "N/A",
                "office_time": "N/A",
                "job_deadline": "N/A",
            })

            time.sleep(1)  # Be polite
        return jobs_data
