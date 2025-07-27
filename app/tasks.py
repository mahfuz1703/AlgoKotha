from celery import shared_task
from app.services.job_scraper import run_all_scrapers

@shared_task
def scrape_all_jobs():
    run_all_scrapers()
