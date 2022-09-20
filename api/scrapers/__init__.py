from scrapers.jobsacuk import JobsacukScraper
from scrapers.findaphd import FindAPhdScraper
from scrapers.Listing import Listing

def scrape_all():
    find_a_phd_scraper = FindAPhdScraper()
    find_a_phd_scraper.scrape()
    return find_a_phd_scraper.listings

    jobs_ac_uk_scraper = JobsacukScraper()
    jobs_ac_uk_scraper.scrape()
    return jobs_ac_uk_scraper.listings
