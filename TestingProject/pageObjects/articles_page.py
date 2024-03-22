from selenium.webdriver.common.by import By


class ArticlesPage:
    article_button = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-machine-dashboard/div/app-machine-efficiency[1]/loe-dashboard-tile/div/div[2]/loe-dashboard-tile/div/loe-line-chart/div/div")

    def __init__(self, driver):
        self.driver = driver

    def return_article_button(self):
        driver = self.driver
        return driver.find_element(*ArticlesPage.article_button)
