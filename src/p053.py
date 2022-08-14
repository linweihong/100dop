# Capstone - data entry project

from pprint import pprint

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from constants import ff_profile, geckodriver_path, google_form

zillow_page = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"


class Scraper:
    def __init__(self):
        self.headers = self.set_headers()
        self.addresses = []

    def set_headers(self):
        return {
            "Accept-Language": "en-GB",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101"
                " Firefox/103.0"
            ),
        }

    def get_site(self, site):
        self.r = requests.get(site, headers=self.headers)
        self.r.raise_for_status()

    def parse_site(self):
        self.soup = BeautifulSoup(self.r.text, "html.parser")
        self.addresses = [
            addr.string.split(" | ")[-1]
            for addr in self.soup.select("address[class='list-card-addr']")
        ]
        self.prices = [
            [string for string in price.stripped_strings][0].strip("/mo").strip("+")
            for price in self.soup.select("div[class='list-card-price']")
        ]
        self.links = [
            l
            if (l := link.get("href")).find("https") == 0
            else f"https://www.zillow.com{l}"
            for link in self.soup.select(
                "a[class='list-card-link list-card-link-top-margin']"
            )
        ]


class FormFiller:
    def __init__(self):
        self.service = Service(executable_path=geckodriver_path)
        self.options = Options()
        self.options.add_argument("-profile")
        self.options.add_argument(ff_profile)

    def submit_form(self, address, price, link):
        self.driver = webdriver.Firefox(service=self.service, options=self.options)
        self.driver.get(google_form)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='button']"))
        )
        self.driver.find_element(
            By.XPATH,
            ".//form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
        ).send_keys(address)
        self.driver.find_element(
            By.XPATH,
            ".//form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
        ).send_keys(price)
        self.driver.find_element(
            By.XPATH,
            ".//form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input",
        ).send_keys(link)
        self.driver.find_element(By.CSS_SELECTOR, "div[role='button']").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='heading']"))
        )
        self.driver.close()


scraper = Scraper()
while not scraper.addresses:
    scraper.get_site(zillow_page)
    scraper.parse_site()
ff = FormFiller()
for i in range(len(scraper.addresses)):
    ff.submit_form(scraper.addresses[i], scraper.prices[i], scraper.links[i])
