import requests
from bs4 import BeautifulSoup
import time

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AlgoKotha.settings')  # Replace with your project name
django.setup()

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
}

main_url = "https://brainstation-23.easy.jobs"
response = requests.get(main_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

job_links = [a['href'] for a in soup.select(".job-header__title a")]

jobs_data = []

for link in job_links:
    print(f"Scraping: {link}")
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
        "title": job_soup.select_one("h1.job-title").text.strip() if job_soup.select_one("h1.job-title") else "N/A",
        "link": link,
        "apply_link": apply_link,
        "meta": job_info,
        "description": job_soup.select_one(".job-description").get_text(separator="\n", strip=True) if job_soup.select_one(".job-description") else "N/A",
        "requirements": job_soup.select_one(".job-requirements").get_text(separator="\n", strip=True) if job_soup.select_one(".job-requirements") else "N/A",
    })

    time.sleep(1)  # be polite and avoid getting blocked

# Print results
for job in jobs_data:
    print(f"Title: {job['title']}")
    print(f"Link: {job['link']}")
    print(f"Apply Link: {job['apply_link']}")
    print(f"Meta: {job['meta']}")
    print(f"Description: {job['description']}")
    print(f"Requirements: {job['requirements']}")
    print("-" * 40)

