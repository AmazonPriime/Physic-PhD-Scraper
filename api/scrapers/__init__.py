from scrapers.jobsacuk import JobsacukScraper
from scrapers.findaphd import FindAPhdScraper
from scrapers.academicpositions import AcademicPositionsScraper
from scrapers.postgradstudentships import PostgradStudentshipsScraper
from scrapers.Listing import Listing

def scrape_all():
    postgrad_studentships_scraper = PostgradStudentshipsScraper()
    postgrad_studentships_scraper.scrape()

    academic_positions_scraper = AcademicPositionsScraper()
    academic_positions_scraper.scrape()

    find_a_phd_scraper = FindAPhdScraper()
    find_a_phd_scraper.scrape()

    jobs_ac_uk_scraper = JobsacukScraper()
    jobs_ac_uk_scraper.scrape()

    job_listings = postgrad_studentships_scraper.listings
    job_listings += academic_positions_scraper.listings
    job_listings += find_a_phd_scraper.listings
    job_listings += jobs_ac_uk_scraper.listings

    return job_listings
