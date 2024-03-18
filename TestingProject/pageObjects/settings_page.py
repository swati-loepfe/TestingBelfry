from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SettingsPage:
    settings_frame = (By.XPATH, "/html/body/app-root/app-shell/div[1]/div[3]/div[2]/app-quick-access/span")
    settings_div = (By.CLASS_NAME, "cdk-overlay-container")

    def __init__(self, driver):
        self.driver = driver

    def settings_button(self):
        driver = self.driver
        return driver.find_element(*SettingsPage.settings_frame)

    def settings_button1(self):
        driver = self.driver
        return driver.find_element(*SettingsPage.settings_div)

