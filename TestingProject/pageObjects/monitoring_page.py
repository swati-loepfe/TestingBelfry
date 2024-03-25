from selenium.webdriver.common.by import By


class MonitoringPage:
    #Main Search/Monitoring button
    search_button = (By.XPATH,"/html/body/app-root/app-shell/div[1]/div[2]/app-navbar/div/span[2]")
    search_compare_button = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/app-tab-bar/div/span[1]")
    search_compare_lastcell1=(By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/div/app-monitoring-compare/div/div[2]/div[1]/loe-dashboard-tile/div/div[2]/app-nslt-matrix/div/div[2]/div[6]/div[1]/span/span")
    search_compare_lastcell2 = (By.XPATH,
                                "/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/div/app-monitoring-compare/div/div[2]/div[1]/loe-dashboard-tile/div/div[2]/app-nslt-matrix/div/div[2]/div[7]/div[1]/span/span")
    search_compare_lastcell3 = (By.XPATH,
                                "/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/div/app-monitoring-compare/div/div[2]/div[1]/loe-dashboard-tile/div/div[2]/app-nslt-matrix/div/div[2]/div[8]/div[1]/span/span")
    search_NSLT_button = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/app-tab-bar/div/span[2]")
    absolute_button = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/div/app-monitoring-compare/div/div[1]/loe-select/div/span[1]")
    event_button=(By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/app-tab-bar/div/span[5]")
    splice_button =(By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/app-tab-bar/div/span[3]")
    bad_positions = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/app-tab-bar/div/span[4]")
    bad_position_cv = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/div/app-monitoring-bad-positions/div/div[2]/table/thead/tr/th[5]/div")
    event_log_title=(By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/div/app-monitoring-event-log/div/loe-dashboard-tile/div/loe-dashboard-tile/div/div")
    search_compare_header = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/div/app-monitoring-compare/div/div[2]/div[1]/loe-dashboard-tile/div/div[1]")
    search_compare_mainheader = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/div/app-monitoring-event-log/div/loe-dashboard-tile/div/div")
    search_compare_header_article2 = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/div/app-monitoring-compare/div/div[2]/div[2]/loe-dashboard-tile/div/div[1]")
    compare_produced_length = (By.XPATH,"/div/span[2]")
    event__arrow_up = (By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/div/app-monitoring-event-log/div/loe-dashboard-tile/div/div/div/span[2]")
    event_bar_down = (By.XPATH,"/div/div[2]/loe-machine-position-chart/div/div[68]/div[1]/div")
    event_Run_Inhibit =(By.XPATH,"/html/body/app-root/app-shell/div[2]/div/app-monitoring/div/div[1]/div/div/app-monitoring-event-log/div/loe-dashboard-tile/div/loe-dashboard-tile/div/cdk-virtual-scroll-viewport/div[1]/div[11]")


    def __init__(self,driver):
        self.driver = driver

    def return_search_button(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.search_button)

    def return_compare_button(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.search_compare_button)

    def return_absolute_button(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.absolute_button)

    def return_NSLT_button(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.search_NSLT_button)

    def return_event_button(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.event_button)

    def return_splice_button(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.splice_button)

    def return_bad_positions(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.bad_positions)

    def return_event_log_title(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.event_log_title)

    def return_event_log_maintitle(self):
        driver=self.driver
        return driver.find_element(*MonitoringPage.search_compare_mainheader)

    def return_compare_header(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.search_compare_header)

    def return_compare_header_article2(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.search_compare_header_article2)

    def return_compare_produced_length(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.compare_produced_length)

    def return_event_arrow(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.event__arrow_up)

    #Change when GUI ID work
    def return_event_bardown(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.event_bar_down)

    def return_event_run_inhibit(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.event_Run_Inhibit)

    def return_compare_lastcell1(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.search_compare_lastcell1)

    def return_compare_lastcell2(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.search_compare_lastcell2)

    def return_compare_lastcell3(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.search_compare_lastcell3)

    def return_bad_position_cv(self):
        driver = self.driver
        return driver.find_element(*MonitoringPage.bad_position_cv)