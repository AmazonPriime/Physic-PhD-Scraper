# scraper for https://academicpositions.com/
from datetime import date
from pydoc import describe
from bs4 import BeautifulSoup
from urls import SiteUrls
from scrapers import Listing
import requests
import re


class PostgradStudentshipsScraper:
    def __init__(self) -> None:
        self.listings = []
        print('Postgraduate Studentships Scraper Initialised')

    def scrape(self):
        response = requests.get(SiteUrls.POSTGRADUATESTUDENTSHIPS)
        soup = BeautifulSoup(response.content, 'html.parser')
        job_listings = soup.find(class_='news-container')
        job_listings = job_listings.find_all(class_='news-item')
        pages = soup.find_all(class_='page-numbers')
        if len(pages) > 0:
            pages = int(pages[-1].get_text())
            for i in range(2, pages + 1):
                response = requests.get(SiteUrls.POSTGRADUATESTUDENTSHIPS.replace('/pn/', f'/pn/{i}#'))
                soup = BeautifulSoup(response.content, 'html.parser')
                soup = soup.find(class_='news-container')
                job_listings = job_listings + soup.find_all(class_='news-item')
        job_listings = list(filter(lambda x: 'featured' not in x.get('class'), job_listings))
        for job in job_listings:
            title = job.h3.get_text().strip()
            link = f"{SiteUrls.POSTGRADUATESTUDENTSHIPS_ROOT}{job.a.get('href')}"
            description = job.p.get_text().strip()
            date_closes = job.h6.get_text().replace('Deadline:', '').strip()
            self.listings.append(Listing.Listing(
                title,
                link,
                'N/A',
                'N/A',
                'N/A',
                description,
                'N/A',
                date_closes,
            ))
