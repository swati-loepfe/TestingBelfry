from selenium.webdriver.common.by import By


class LoginPage:
    login_button = (By.XPATH, "/html/body/app-root/app-shell/div[1]/div[3]/div[1]/app-login/div/span")
    login_password = (By.XPATH, "//*[@id='cdk-dialog-0']/app-login-dialog/loe-dashboard-tile/div/div[2]/loe-input")
    login_keyboard = (By.XPATH, "/html/body/app-root/loe-keyboard-loader/loe-keyboard/div[2]/input")
    login_check1 =(By.XPATH,"/html/body/app-root/loe-keyboard-loader/loe-keyboard/div[2]/div/div/div[5]/div[3]")
    login_check2 =(By.XPATH,"/html/body/div/div[2]/div/cdk-dialog-container/app-login-dialog/loe-dashboard-tile/div/div[2]/div/loe-button[2]/div/div/span")
    ##Input keyboard key
    # driver.find_element_by_xpath(
    #    "//*[@id='cdk-dialog-0']/app-login-dialog/loe-dashboard-tile/div/div[2]/loe-input").click()
    #driver.find_element_by_xpath("/html/body/app-root/loe-keyboard-loader/loe-keyboard/div[2]/input").send_keys(123)


    def __init__(self,driver):
        self.driver = driver

    def return_login_button(self):
        driver = self.driver
        return driver.find_element(*LoginPage.login_button)

    def return_login_password(self):
        driver = self.driver
        return driver.find_element(*LoginPage.login_password)

    def return_login_keyboard(self):
        driver = self.driver
        return driver.find_element(*LoginPage.login_keyboard)

#THis is for setting 123 password
    def return_set_password(self):
        driver = self.driver
        return driver.find_element(*LoginPage.login_keyboard)

    def return_login_check1(self):
        driver = self.driver
        return driver.find_element(*LoginPage.login_check1)

    def return_login_check2(self):
        driver = self.driver
        return driver.find_element(*LoginPage.login_check2)