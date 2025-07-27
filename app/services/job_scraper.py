from app.models import Companies, Jobs
from app.scraper import get_scraper

def run_all_scrapers():
    for company in Companies.objects.all():
        scraper = get_scraper(company)
        if scraper is None:
            print(f"No scraper found for {company.name}")
            continue

        try:
            job_data = scraper.scrape_jobs()
            for job in job_data:
                Jobs.objects.get_or_create(
                    company=company,
                    job_link=job.get('job_link'),
                    job_apply_link=job.get('job_apply_link'),
                    job_title=job.get('job_title'),
                    job_vacancies=job.get('job_vacancies', 0),
                    job_salary=job.get('job_salary'),
                    job_salary_type=job.get('job_salary_type'),
                    office_time=job.get('office_time'),
                    job_type=job.get('job_type'),
                    job_location=job.get('job_location'),
                    job_deadline=job.get('job_deadline'),
                )
        except Exception as e:
            print(f"Error scraping {company.name}: {e}")
