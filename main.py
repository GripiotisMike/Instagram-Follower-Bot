from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

INSTA_EMAIL = os.getenv("INSTA_EMAIL")
INSTA_PASS = os.getenv("INSTA_PASS")
INSTA_USER = os.getenv("INSTA_USER")


class InstaFollower:
    def __init__(self):
        # Configure Chrome driver options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        """Logs in to Instagram with provided credentials."""
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        # Decline cookie consent if prompted
        decline = self.driver.find_element(By.XPATH,
                                           '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        decline.click()
        time.sleep(2)

        # Input email and password
        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(f"{INSTA_EMAIL}{Keys.TAB}{INSTA_PASS}{Keys.ENTER}")
        time.sleep(5)

        # Handle "Save Login Info" and "Turn on Notifications" pop-ups
        save_login_prompt = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()
        time.sleep(4)

        notifications_prompt = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        """Navigates to a target profile's followers list and scrolls through it."""
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{INSTA_USER}/followers")
        time.sleep(6)

        # Scroll the followers modal to load more followers
        modal = self.driver.find_element(By.XPATH,
                                         "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        for _ in range(5):  # Scroll 5 times
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        """Attempts to follow users from the followers list."""
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, '._aano button')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel_button.click()


if __name__ == "__main__":
    bot = InstaFollower()
    bot.login()
    bot.find_followers()
    bot.follow()
