from scrapers.jobsacuk import JobsacukScraper
from scrapers.findaphd import FindAPhdScraper
from scrapers.academicpositions import AcademicPositionsScraper
from scrapers.Listing import Listing

def scrape_all():
    academic_positions_scraper = AcademicPositionsScraper()
    academic_positions_scraper.scrape()
    return academic_positions_scraper.listings

    find_a_phd_scraper = FindAPhdScraper()
    find_a_phd_scraper.scrape()
    return find_a_phd_scraper.listings

    jobs_ac_uk_scraper = JobsacukScraper()
    jobs_ac_uk_scraper.scrape()
    return jobs_ac_uk_scraper.listings
