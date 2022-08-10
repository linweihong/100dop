# Cookie Clicker

import datetime as dt

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from constants import ff_profile, geckodriver_path


def setup_driver() -> webdriver:
    service = Service(executable_path=geckodriver_path)
    options = Options()
    options.add_argument("-profile")
    options.add_argument(ff_profile)
    driver = webdriver.Firefox(service=service, options=options)
    return driver


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


# def hover(element):
#     action = ActionChains(driver)
#     action.move_to_element(element).perform()


driver = setup_driver()  # Initiate driver
driver.get("https://orteil.dashnet.org/cookieclicker/")  # Load webpage

cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')  # Find cookie
WebDriverWait(driver, 10).until(
    expected_conditions.invisibility_of_element_located((By.ID, "offGameMessage"))
)  # Wait for cookie to be clickable

while True:
    start_clock = dt.datetime.now()
    while dt.datetime.now() - start_clock < dt.timedelta(
        seconds=30
    ):  # Check store every 30 seconds
        cookie.click()
    while upgrades := driver.find_elements(
        By.CSS_SELECTOR, "div.crate.upgrade.enabled"
    ):  # Purchase most expensive upgrade
        upgrades[-1].click()
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
    ):  # Purchase most expensive product
        products[-1].click()
