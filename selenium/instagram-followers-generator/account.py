from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InstaAccount:
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)


    def login(self, username, password) -> None:
        """Log in to the user's instagram account."""
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")

        username_input.send_keys(username) # enter username
        password_input.send_keys(password) # enter password
        time.sleep(2)
        password_input.send_keys(Keys.ENTER) # click enter
        time.sleep(4)

        # if pops up 'Save Info' option, click "Save Info"
        self.click_if_exists("Save Info")
        # if pops up 'Turn On Notifications' option, click "Not Now"
        self.click_if_exists("Not Now")
            

    def follow_all_followers(self, similar_account) -> None:
        """Follows every follower of a given Instagram account."""
        self.driver.get(f"https://www.instagram.com/{similar_account}/followers/")
        time.sleep(5)

        self.click_if_exists("Follow")


    def click_if_exists(self, btn_text) -> None:
        """Click on the button named <btn_text> if exists."""
        btns = self.driver.find_elements(By.TAG_NAME, "button")
        for btn in btns:
            if btn.text == btn_text:
                btn.click()
                time.sleep(1)


    def close_driver(self) -> None:
        """Closes the driver."""
        self.driver.quit()