# Cookie Clicker

import datetime as dt
import os
import sys

from selenium import webdriver
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        WebDriverException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from constants import chrome_data, chrome_profile, chromedriver_path


def setup_driver() -> webdriver:
    service = Service(executable_path=chromedriver_path)
    options = Options()
    options.add_argument(f"--user-data-dir={chrome_data}")
    options.add_argument(f"--profile-directory={chrome_profile}")
    # options.add_argument("-headless")
    driver = webdriver.Chrome(service=service, options=options)
    return driver


# def cps_per_cookie(element):
#     hover_mouse(element)
#     if driver.find_element(By.CSS_SELECTOR, "#tooltipBuilding .descriptionBlock b"):
#         hover_mouse(element)
#         cps = float(
#             driver.find_element(By.CSS_SELECTOR, "#tooltipBuilding .descriptionBlock b")
#             .text.split(" ")[0]
#             .replace(",", "")
#         )
#     else:
#         return 0
#     hover_mouse(element)
#     price = int(
#         driver.find_element(
#             By.CSS_SELECTOR, "#tooltipBuilding span.price"
#         ).text.replace(",", "")
#     )
#     print(f"{price/cps=}")
#     return price / cps


def hover_mouse(element):
    ActionChains(driver).move_to_element(cookie).perform()
    ActionChains(driver).move_to_element(element).perform()


def golden_cookie():
    gc = driver.find_element(By.ID, "goldenCookie")
    try:
        gc.click()
        print("Golden cookie clicked.")
    except WebDriverException:
        pass


# def buy_best_upgrade():
#     if (
#         len(
#             products := driver.find_elements(
#                 By.CSS_SELECTOR, "div.product.unlocked.enabled"
#             )
#         )
#         > 1
#     ):
#         best_product = products[0]
#         for product in products[1:]:
#             if cps_per_cookie(product) > cps_per_cookie(best_product):
#                 best_product = product
#         best_product.click()
#         buy_best_upgrade()
#     elif len(products) == 1:
#         products[0].click()
#     else:
#         return


# def get_prices() -> dict:
#     return {
#         f"product{i}": int(price.replace(",", ""))
#         for i in range(19)
#         if (price := driver.find_element(By.ID, f"productPrice{i}").text)
#     }


# def get_cookies() -> int:
#     return int(
#         driver.find_element(By.ID, "cookies").text.split(" ")[0].replace(",", "")
#     )


def run_time():
    run_time = dt.datetime.now() - program_start
    minutes, seconds = divmod(run_time.seconds, 60)
    sys.stdout.write(f"\rRuntime: {minutes}:{seconds:02} ...".ljust(terminal_width))
    sys.stdout.flush()


terminal_width = os.get_terminal_size().columns

driver = setup_driver()  # Initiate driver
driver.get("https://orteil.dashnet.org/cookieclicker/")  # Load webpage

cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')  # Find cookie
WebDriverWait(driver, 10).until(
    expected_conditions.invisibility_of_element_located((By.ID, "offGameMessage"))
)  # Wait for cookie to be clickable

program_start = dt.datetime.now()

while True:
    start_clock = dt.datetime.now()
    while dt.datetime.now() - start_clock < dt.timedelta(
        seconds=12
    ):  # Check store every 12 seconds
        try:
            cookie.click()
        except ElementClickInterceptedException:
            golden_cookie()
    hover_mouse(driver.find_element(By.ID, "upgrades"))
    while upgrades := driver.find_elements(
        By.CSS_SELECTOR, "div.crate.upgrade.enabled"
    ):  # Purchase most expensive upgrade
        upgrades[-1].click()
        hover_mouse(driver.find_element(By.ID, "upgrades"))
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
    while products := driver.find_elements(
        By.CSS_SELECTOR, "div.product.unlocked.enabled"
    ):
        products[-1].click()
    golden_cookie()
    run_time()
