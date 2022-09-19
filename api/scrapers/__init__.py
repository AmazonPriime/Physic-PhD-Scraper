from scrapers.jobsacuk import JobsacukScraper
from scrapers.Listing import Listing

def scrape_all():
    jobs_ac_uk_scraper = JobsacukScraper()
    jobs_ac_uk_scraper.scrape()
    return jobs_ac_uk_scraper.listings
