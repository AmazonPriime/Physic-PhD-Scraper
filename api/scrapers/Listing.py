import re

def clean_spaces(string):
    return re.sub(' +', ' ', string)

class Listing:
    def __init__(self, title, link, employer, location, salary, date_placed, date_closes) -> None:
        self.title = title
        self.link=link
        self.employer=employer
        self.location=location
        self.salary=salary
        self.date_placed=date_placed
        self.date_closes=date_closes

    def export(self):
        return {
            'title': clean_spaces(self.title),
            'link': clean_spaces(self.link),
            'employer': clean_spaces(self.employer),
            'location': clean_spaces(self.location),
            'salary': clean_spaces(self.salary),
            'date_placed': clean_spaces(self.date_placed),
            'date_closes': clean_spaces(self.date_closes)
        }
