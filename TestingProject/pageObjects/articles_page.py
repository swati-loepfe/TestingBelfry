from selenium.webdriver.common.by import By


class ArticlesPage:
    #article_button = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-machine-dashboard/div/app-machine-efficiency[1]/loe-dashboard-tile/div/div[2]/loe-dashboard-tile/div/loe-line-chart/div/div")
    article_button = (By.XPATH,"/html/body/app-root/app-screen-saver/div[2]/div/div/div/div[1]/div[1]/div[2]")
    articles_main_button =(By.XPATH,"/html/body/app-root/app-shell/div[1]/div[2]/app-navbar/div/span[3]")
    articles_edit_article_lower =(By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-article-settings/div[2]/div/table/tbody/tr/td[1]/loe-article-select/div/div/span")
    articles_slider_button = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-article-settings/div[2]/div/table/tbody/tr/td[3]/div/div[1]/loe-switch/label/span")
    articles_edit_save_changes =(By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-article-settings/div[1]/div[2]/loe-button/div/div/span")

    def __init__(self, driver):
        self.driver = driver

    def return_article_button(self):
        driver = self.driver
        return driver.find_element(*ArticlesPage.article_button)

    def return_articles_main_button(self):
        driver = self.driver
        return driver.find_element(*ArticlesPage.articles_main_button)

    def return_articles_edit_article_lower(self):
        driver = self.driver
        return driver.find_element(*ArticlesPage.articles_edit_article_lower)

    def return_articles_slider_button(self):
        driver = self.driver
        return driver.find_element(*ArticlesPage.articles_slider_button)

    def return_articles_save_changes(self):
        driver = self.driver
        return driver.find_element(*ArticlesPage.articles_edit_save_changes)