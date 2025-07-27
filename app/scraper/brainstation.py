import requests
from bs4 import BeautifulSoup
from .base import BaseScraper
import time

class BrainStationScraper(BaseScraper):
    def scrape_jobs(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
        }

        response = requests.get(self.company.careerPage, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        job_links = [a['href'] for a in soup.select(".job-header__title a")]

        jobs_data = []

        for link in job_links:
            job_resp = requests.get(link, headers=headers)
            job_soup = BeautifulSoup(job_resp.text, "html.parser")

            overview_items = job_soup.select(".job-overview__list-item")

            job_info = {}

            for item in overview_items:
                label = item.select_one(".job-overview__list-item-label")
                value = item.select_one(".job-overview__list-item-value")
                if label and value:
                    job_info[label.text.strip()] = value.get_text(separator=" ", strip=True)

            apply_link_tag = job_soup.select_one(".job-overview__footer-left a")
            apply_link = apply_link_tag['href'] if apply_link_tag else "N/A"

            jobs_data.append({
                "job_link": link,
                "job_apply_link": apply_link,
                "job_title": job_info.get('Job Title', 'N/A'),
                "job_vacancies": job_info.get('Vacancies', 0),
                "job_salary": job_info.get('Salary', 'N/A'),
                "job_salary_type": job_info.get('Salary Type', 'N/A'),
                "office_time": job_info.get('Office Time', 'N/A'),
                "job_type": job_info.get('Job Type', 'N/A'),
                "job_location": job_info.get('Location', 'N/A'),
                "job_deadline": job_info.get('Deadline', 'N/A'),
            })

            time.sleep(1)  # be polite and avoid getting blocked
        return jobs_data
