import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pageObjects import monitoring_page
from pageObjects.login_page import LoginPage
from pageObjects.screensaver_page import ScreensaverPage
from pageObjects.monitoring_page import MonitoringPage
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
    driver.close()


def test_first_click(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    driver.close()


def test_login_page_correctpassword(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    loginpage=LoginPage(driver)
    loginpage.return_login_button().click()
    loginpage.return_login_password().click()
    loginpage.return_login_keyboard().click()
    loginpage.return_set_password().send_keys(123)
    loginpage.return_login_check1().click()
    loginpage.return_login_check2().click()

def test_login_page_incorrectpassword(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    loginpage=LoginPage(driver)
    loginpage.return_login_button().click()
    loginpage.return_login_password().click()
    loginpage.return_login_keyboard().click()
    loginpage.return_set_password().send_keys(1234)
    loginpage.return_login_check1().click()
    loginpage.return_login_check2().click()
    time.sleep(10)
    loginpage.return_incorrect_password().click()
    #invoke virtual keyboard again
    loginpage.return_login_password().click()
    loginpage.return_login_keyboard().click()
    loginpage.return_set_password().send_keys(123)
    loginpage.return_login_check1().click()
    loginpage.return_login_check2().click()


def test_settings(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(50)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    loginpage = LoginPage(driver)
    loginpage.return_login_button().click()
    loginpage.return_login_password().click()
    loginpage.return_login_keyboard().click()
    loginpage.return_set_password().send_keys(123)
    loginpage.return_login_check1().click()
    loginpage.return_login_check2().click()
    settingspage = SettingsPage(driver)
    time.sleep(10)
    settingspage.settings_button().click()
    time.sleep(10)
    settingspage.settings_button1().click()
    driver.close()

def test_monitoring_click_alltabs(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    searchpage=MonitoringPage(driver)
    time.sleep(10)
    searchpage.return_search_button().click()
    time.sleep(5)
    searchpage.return_NSLT_button().click()
    time.sleep(5)
    searchpage.return_splice_button().click()
    time.sleep(5)
    searchpage.return_bad_positions().click()
    time.sleep(5)
    searchpage.return_compare_button().click()
    time.sleep(5)
    searchpage.return_event_button().click()


def test_Monitoring_Event_log(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(50)
    # Navigate to Article Dashboard
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    time.sleep(5)
    monitoring_page= MonitoringPage(driver)
    time.sleep(1)
    monitoring_page.return_search_button().click()
    time.sleep(1)
    monitoring_page.return_event_button().click()
    time.sleep(3)
    assert monitoring_page.return_event_log_title().text == "Event\nTimestamp"






