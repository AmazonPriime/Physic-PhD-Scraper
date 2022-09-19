# scraper for https://www.jobs.ac.uk/
from bs4 import BeautifulSoup
from urls import SiteUrls
from scrapers import Listing
import requests
import re


class JobsacukScraper:
    def __init__(self) -> None:
        self.listings = []
        print('Jobs.ac.uk Scraper Initialised')

    def scrape(self):
        response = requests.get(SiteUrls.JOBSACUK)
        soup = BeautifulSoup(response.content, 'html.parser')
        job_listings = soup.find(id='job-listings').find_all('div', recursive=False)
        for job in job_listings:
            try:
                title = job.a.get_text().strip()
                link = f"{SiteUrls.JOBSACUK_ROOT}{job.a.get('href').strip()}"
                employer = job.find(class_='j-search-result__employer')
                employer = employer.get_text().strip()
                location = job.find(class_='j-search-result__text').find_all('div', recursive=False)[2]
                location = location.get_text().split(':')[-1].strip()
                salary = job.find(class_='j-search-result__info').get_text()
                salary = salary.split(':')[-1].strip()
                date_placed = job.find(class_='j-search-result__text').find_all('div')[-1]
                date_placed = re.search(r'\d\d \w+', date_placed.get_text()).group(0)
                date_closes = job.find(class_='j-search-result__date--blue').get_text()
                self.listings.append(Listing.Listing(
                    title,
                    link,
                    employer,
                    location,
                    salary,
                    date_placed,
                    date_closes,
                ))
            except Exception as e:
                print('Issue processing one of the listings.')
                print(job)
                print('-'*10)
                print(e)
                break


