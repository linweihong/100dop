# Twitter bot

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from constants import chrome_data, chrome_profile, chromedriver_path


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.down = 0
        self.up = 0
        self.setup_driver()

    def setup_driver(self):
        self.service = Service(executable_path=chromedriver_path)
        self.options = Options()
        self.options.add_argument(f"--user-data-dir={chrome_data}")
        self.options.add_argument(f"--profile-directory={chrome_profile}")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(
            By.XPATH, ".//a[@class='js-start-test test-mode-multi']"
        ).click()
        WebDriverWait(self.driver, 45).until(
            expected_conditions.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "span.result-data-large.number.result-data-value.upload-speed",
                )
            )
        )
        while True:
            try:
                self.up = float(
                    self.driver.find_element(
                        By.CSS_SELECTOR,
                        "span.result-data-large.number.result-data-value.upload-speed",
                    ).text
                )
            except ValueError:
                pass
            else:
                break
        self.down = float(
            self.driver.find_element(
                By.CSS_SELECTOR,
                "span.result-data-large.number.result-data-value.download-speed",
            ).text
        )

    def tweet_at_provider(self):
        pass


istb = InternetSpeedTwitterBot()
istb.get_internet_speed()
