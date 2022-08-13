# Twitter bot

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from constants import (TWITTER_PWD, TWITTER_USER, TWITTER_USN, chrome_data,
                       chrome_profile, chromedriver_path)

TIMEOUT_TIME = 2


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.down = 0
        self.up = 0
        self.driver = self.setup_driver()

    def setup_driver(self):
        service = Service(executable_path=chromedriver_path)
        options = Options()
        options.add_argument(f"--user-data-dir={chrome_data}")
        options.add_argument(f"--profile-directory={chrome_profile}")
        return webdriver.Chrome(service=service, options=options)

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
        self.driver.get("https://twitter.com/i/flow/login")
        self.t_login()
        self.post_tweet()

    def t_login(self):
        WebDriverWait(self.driver, TIMEOUT_TIME).until(
            expected_conditions.presence_of_element_located((By.NAME, "text"))
        )
        self.driver.find_element(By.NAME, "text").send_keys(TWITTER_USER)
        self.driver.find_element(
            By.XPATH,
            ".//div/div/div[2]/div[2]/div/div/div/div[6]",
        ).click()
        try:
            WebDriverWait(self.driver, TIMEOUT_TIME).until(
                expected_conditions.presence_of_element_located((By.NAME, "password"))
            )
        except TimeoutException:
            self.driver.find_element(
                By.CSS_SELECTOR, "input[data-testid='ocfEnterTextTextInput']"
            ).send_keys(TWITTER_USN)
            self.driver.find_element(
                By.CSS_SELECTOR, "div[data-testid='ocfEnterTextNextButton']"
            ).click()
        finally:
            WebDriverWait(self.driver, TIMEOUT_TIME).until(
                expected_conditions.presence_of_element_located((By.NAME, "password"))
            )
            self.driver.find_element(By.NAME, "password").send_keys(TWITTER_PWD)
        self.driver.find_element(
            By.CSS_SELECTOR, "div[data-testid='LoginForm_Login_Button']"
        ).click()

    def post_tweet(self):
        WebDriverWait(self.driver, TIMEOUT_TIME).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, 'a[data-testid="SideNav_NewTweet_Button"]')
            )
        )
        self.driver.find_element(
            By.CSS_SELECTOR, 'a[data-testid="SideNav_NewTweet_Button"]'
        ).click()
        WebDriverWait(self.driver, TIMEOUT_TIME).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0"]')
            )
        )
        self.driver.find_element(
            By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0"]'
        ).send_keys(self.message())
        self.driver.find_element(
            By.CSS_SELECTOR, 'div[data-testid="tweetButton"]'
        ).click()

    def message(self):
        return f"My Internet speed is only {self.down} Mbps down and {self.up} Mbps up!"


istb = InternetSpeedTwitterBot()
istb.get_internet_speed()
istb.tweet_at_provider()
