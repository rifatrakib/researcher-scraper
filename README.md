# Researcher Scraper

This project aims to collect information about master's supervisors from different universities from their official pages in the corresponding university website. The purpose is to reduce the time required to browse hundreds of pages to collect the required information. The collected data gives a jumpstart in researching potential supervisors from master's program by focusing on collecting research interests of each professor and thereby providing a quick shortlist to start preparing for master's applications.

## Description

This project contains a single scraper containing multiple spiders, one for each university. The prerequisite is that the pages containing the information about the faculty members must have a regular format for each universities. The reason behind building different spiders for different universities is because of different structure of the HTMLs used by the institutions. The output data are stored as JSON files and Excel spreadsheets named after the scraper name which follows the short-hand names of the corresponding universities.

## Getting Started

### Dependencies

* Python 3.9 or higher.

### Installing

* Clone the repository:

```
git clone https://github.com/rifatrakib/researcher-scraper.git
```

### Executing program

* Create a python virtual environment. (Highly recommended)
* Install the project dependencies:

```
pip install poetry
poetry install
```

* Run the scraper (spider_name can be found in the spider files):

```
scrapy crawl <spider_name>
```
