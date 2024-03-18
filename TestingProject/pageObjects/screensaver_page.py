from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ScreensaverPage:
    screensaver_frame = (By.XPATH, "/html/body/app-root/app-screen-saver/div[2]/div/div/div/div[1]/div[1]")

    def __init__(self, driver):
        self.driver = driver

    def screensaver_button(self):
        driver = self.driver
        return driver.find_element(*ScreensaverPage.screensaver_frame)


