# scraper for https://academicpositions.com/
from datetime import date
from bs4 import BeautifulSoup
from urls import SiteUrls
from scrapers import Listing
import requests
import re


class AcademicPositionsScraper:
    def __init__(self) -> None:
        self.listings = []
        print('Academic Positions Scraper Initialised')

    def scrape(self):
        response = requests.get(SiteUrls.ACADEMICPOSITIONS)
        soup = BeautifulSoup(response.content, 'html.parser')
        job_listings = soup.find(id='list-jobs-results').find_all(class_='list-group')
        pages = soup.find_all(class_='page-link')
        if pages:
            pages = int(pages[-2].get_text())
            for i in range(2, pages + 1):
                response = requests.get(SiteUrls.ACADEMICPOSITIONS + f'&page={i}')
                soup = BeautifulSoup(response.content, 'html.parser')
                job_listings = job_listings + soup.find(id='list-jobs-results').find_all(class_='list-group')

        for job in job_listings:
            title = job.h4.get_text().strip()
            link = f"{SiteUrls.ACADEMICPOSITIONS_ROOT}{job.find(class_='hover-title-underline').get('href')}"
            employer = job.a.get_text().strip()
            location = job.find(class_='text-muted').get_text().strip()
            salary = 'N/A'
            description = job.find(class_='hover-title-underline').p.get_text().strip()
            dates = job.find(class_='row-tight').get_text()
            dates = re.sub(' +', ' ', dates).replace('\n', '').split('  ')
            date_placed = dates[0].strip() if len(dates) > 0 else 'N/A'
            date_closes = dates[1].strip() if len(dates) > 1 else 'N/A'
            if not ('Published' in date_placed):
                date_placed = 'N/A'
            if not ('Closing in' in date_closes):
                date_closes = 'N/A'
            date_placed = date_placed.replace('Published', '')
            date_closes = date_closes.replace('Closing in', '')
            self.listings.append(Listing.Listing(
                title,
                link,
                employer,
                location,
                'N/A',
                description,
                date_placed,
                date_closes,
            ))
