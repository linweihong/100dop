# Cookie Clicker

import datetime as dt
import os
import sys
from xml.dom.minidom import Element

from selenium import webdriver
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        StaleElementReferenceException,
                                        WebDriverException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from constants import chrome_data, chrome_profile, chromedriver_path


class CookieClicker:
    def __init__(self):
        self.avg_cps = 0.0
        self.c = 0  # Cookies collected over runtime
        self.t = 0
        self.upgrades = []
        self.products = []
        self.driver = self.setup_driver()  # Load driver
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")  # Get webpage
        self.cookie = self.driver.find_element(
            By.XPATH, '//*[@id="bigCookie"]'
        )  # Find cookie
        self.gc = self.driver.find_element(By.ID, "goldenCookie")  # Find golden cookie
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(
                (By.ID, "offGameMessage")
            )
        )  # Wait for cookie to be clickable
        self.start = dt.datetime.now()  # Start program clock
        self.cookies = self.get_cookies()  # Establish base average cps
        self.cps = int(
            self.get_element_text(By.ID, "cookiesPerSecond")
            .split(" ")[-1]
            .replace(",", "")
        )
        self.click_cookie(12)

    def setup_driver(self) -> webdriver:
        self.service = Service(executable_path=chromedriver_path)
        self.options = Options()
        self.options.add_argument(f"--user-data-dir={chrome_data}")
        self.options.add_argument(f"--profile-directory={chrome_profile}")
        # options.add_argument("-headless")
        return webdriver.Chrome(
            service=self.service,
            options=self.options,
        )

    def cps_per_cookie(self, element):
        self.hover_mouse(element=element)
        if t := self.get_element_text(
            By.CSS_SELECTOR, "div#tooltipBuilding div.descriptionBlock b"
        ):

            cps = float(t.split(" ")[0].replace(",", ""))
        else:
            return 0
        self.hover_mouse(element=element)
        price = int(
            self.get_element_text(
                By.CSS_SELECTOR, "div#tooltipBuilding span.price"
            ).replace(",", "")
        )
        return price / cps

    def find_element(self, by, search_term):
        return self.driver.find_element(by, search_term)

    def find_elements(self, by, search_term):
        return self.driver.find_elements(by, search_term)

    def hover_mouse(self, by=None, search_term=None, element=None):
        if not element:
            element = self.driver.find_element(by, search_term)
        ActionChains(self.driver).move_to_element(self.cookie).perform()
        ActionChains(self.driver).move_to_element(element).perform()

    def golden_cookie(self):
        try:
            self.gc.click()
            print("Golden cookie clicked.")
        except WebDriverException:
            pass

    def buy_best_product(self):
        if (
            len(
                products := self.driver.find_elements(
                    By.CSS_SELECTOR, "div.product.unlocked.enabled"
                )
            )
            > 1
        ):
            best_product = products[0]
            for p in products[1:]:
                if self.cps_per_cookie(p) > self.cps_per_cookie(best_product):
                    best_product = p
            while "enabled" in best_product.get_attribute("class"):
                best_product.click()
        elif len(products) == 1:
            while "enabled" in products[0].get_attribute("class"):
                products[0].click()
        else:
            return

    def get_prices(self) -> dict:
        return {
            f"product{i}": int(price.replace(",", ""))
            for i in range(19)
            if (price := self.driver.find_element(By.ID, f"productPrice{i}").text)
        }

    def get_cookies(self) -> int:
        self.cookies = int(
            self.get_element_text(By.ID, "cookies").split()[0].replace(",", "")
        )
        return self.cookies

    def eval_next_upgrade(self):
        if not self.avg_cps:
            return False
        # products = self.driver.find_elements(
        #     By.CSS_SELECTOR, "div#products div.product.unlocked div.content span.price"
        # )
        products = self.driver.find_elements(
            By.CSS_SELECTOR, "div#products div.product.unlocked"
        )
        next_upgrade_price = int(
            products[-1]
            .find_element(By.CSS_SELECTOR, "span.price")
            .text.replace(",", "")
        )
        # next_upgrade_price = int(products[-1].text.replace(",", ""))
        if (
            t := ((next_upgrade_price - self.cookies) / self.cps)
        ) < 60 * 10:  # Cause script to wait if next upgrade is within 10 minutes
            self.click_cookie(round(t))
            products[-1].click()

    def announce_run_time(self):
        self.run_time = dt.datetime.now() - self.start
        minutes, seconds = divmod(self.run_time.seconds, 60)
        print(f"\rRuntime: {minutes}:{seconds:02} ...")

    def click_cookie(self, t):
        "Clicks the cookie for t seconds."
        start_cookies = self.get_cookies()
        start_clock = dt.datetime.now()
        print(f"Clicking for {t:02,} seconds ...")
        while dt.datetime.now() - start_clock < dt.timedelta(seconds=t):
            try:
                self.cookie.click()
            except ElementClickInterceptedException:
                self.golden_cookie()
        end_cookies = self.get_cookies()
        self.update_avg_cps(end_cookies - start_cookies, t)

    def update_avg_cps(self, c, t):
        self.c += c
        self.t += t
        self.avg_cps = self.c / self.t

    def fetch_upgrades(self):
        self.hover_mouse(By.ID, "upgrades")
        self.upgrades = self.find_elements(By.CSS_SELECTOR, "div.crate.upgrade.enabled")
        return self.upgrades

    def buy_latest_upgrade(self):
        self.upgrades[-1].click()

    def fetch_products(self):
        self.products = self.find_elements(
            By.CSS_SELECTOR, "div.product.unlocked.enabled"
        )
        return self.products

    def get_element_text(self, by, search_term):
        while True:
            try:
                return self.find_element(by, search_term).text
            except StaleElementReferenceException:
                pass


cc = CookieClicker()

while True:
    cc.eval_next_upgrade()
    cc.click_cookie(12)
    while cc.fetch_upgrades():
        cc.buy_latest_upgrade()
        # while (cheapest_product := min((store := get_prices()).values())) < (
        #     cookies := get_cookies()
        # ):  # Sufficient cookies to make a purchase
        #     most_expensive_product = ["", cookies - cheapest_product]
        #     for key in store:
        #         if (
        #             change := cookies - store[key]
        #         ) >= 0 and change <= most_expensive_product[1]:
        #             most_expensive_product[0] = key
        #             most_expensive_product[1] = change
        #     driver.find_element(By.ID, most_expensive_product[0]).click()
    while cc.fetch_products():
        cc.buy_best_product()
    cc.announce_run_time()
