from selenium.webdriver.common.by import By


class SearchPage:
    search_button = (By.XPATH,"/html/body/app-root/app-shell/div[1]/div[2]/app-navbar/div/span[2]")
    search_compare_button = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/app-tab-bar/div/span[2]")
    absolute_button = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/div/app-monitoring-compare/div/div[1]/loe-select/div/span[1]")

    def __init__(self,driver):
        self.driver = driver

    def return_search_button(self):
        driver = self.driver
        return driver.find_element(*SearchPage.search_button)

    def return_compare_button(self):
        driver = self.driver
        return driver.find_element(*SearchPage.search_compare_button)

    def return_absolute_button(self):
        driver = self.driver
        return driver.find_element(*SearchPage.absolute_button)
