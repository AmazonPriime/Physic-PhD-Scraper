# scraper for http://findaphd.com/
from datetime import date
from bs4 import BeautifulSoup
from urls import SiteUrls
from scrapers import Listing
import requests
import re


class FindAPhdScraper:
    def __init__(self) -> None:
        self.listings = []
        print('Find a PhD Scraper Initialised')

    def scrape(self):
        response = requests.get(SiteUrls.FINDAPHD)
        soup = BeautifulSoup(response.content, 'html.parser')
        job_listings = soup.find(id='SearchResults').find_all(class_='phd-result-row-standard')
        pages = int(soup.find(class_='pagination').find_all('li')[-1].get_text())
        for i in range(2, pages + 1):
            response = requests.get(SiteUrls.FINDAPHD + f'&PG={i}')
            soup = BeautifulSoup(response.content, 'html.parser')
            job_listings = job_listings + soup.find(id='SearchResults').find_all(class_='phd-result-row-standard')
        for job in job_listings:
            title = job.h3.get_text().strip()
            link = f"{SiteUrls.FINDAPHD_ROOT}{job.a.get('href')}"
            employer = job.find(class_='instDeptRow').get_text().strip()
            employer = employer.replace('\n\n', ', ')
            salary = job.find(class_='phd-icon-area').a.get_text().strip()
            description = job.find(class_='descFrag').get_text().strip()
            description = description.replace('Read more', '')
            date_placed = job.find(class_='small').get_text()
            date_placed = date_placed.split(':')[-1].strip()
            self.listings.append(Listing.Listing(
                title,
                link,
                employer,
                'N/A',
                salary,
                description,
                date_placed,
                'N/A',
            ))



