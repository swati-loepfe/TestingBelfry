import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from pageObjects.login_page import LoginPage
from pageObjects.screensaver_page import ScreensaverPage
from pageObjects.monitoring_page import SearchPage
from pageObjects.settings_page import SettingsPage
from testCases.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestLogin(BaseClass):
    baseURL = "http://13.68.159.147/"


def test_openPage(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.quit()


def test_first_click(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()


def test_monitor_click(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    searchpage=SearchPage(driver)
    searchpage.return_search_button().click()
    searchpage.return_absolute_button().click()
    searchpage.return_compare_button().click()


def test_login_page(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    searchpage = SearchPage(driver)
    searchpage.return_search_button().click()
    searchpage.return_absolute_button().click()
    searchpage.return_compare_button().click()
    loginpage=LoginPage(driver)
    loginpage.return_login_button().click()
    loginpage.return_login_password().click()
    loginpage.return_login_keyboard().click()
    loginpage.return_set_password().send_keys(123)
    loginpage.return_login_check1().click()
    loginpage.return_login_check2().click()

def test_settings(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    loginpage = LoginPage(driver)
    loginpage.return_login_button().click()
    loginpage.return_login_password().click()
    loginpage.return_login_keyboard().click()
    driver.implicitly_wait(30)
    loginpage.return_set_password().send_keys(123)
    loginpage.return_login_check1().click()
    loginpage.return_login_check2().click()
    settingspage = SettingsPage(driver)
    settingspage.settings_button().click()
    settingspage.settings_button1().click()




