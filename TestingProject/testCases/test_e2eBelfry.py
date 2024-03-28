import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pageObjects.login_page import LoginPage
from pageObjects.screensaver_page import ScreensaverPage
from pageObjects.monitoring_page import MonitoringPage
from pageObjects.settings_page import SettingsPage
from pageObjects.articles_page import ArticlesPage
from testCases.BaseClass import BaseClass


@pytest.mark.usefixtures("setup", "log_on_failure")
class TestLogin:
    baseURL = "http://13.68.159.147/"
    #baseURL="http://localhost/"


def test_openPage(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    #driver.close()


#def test_navigate_machinedashboard(setup):
 #   driver = setup
  #  driver.get(TestLogin.baseURL)
   # driver.maximize_window()
   # driver.implicitly_wait(20)
    #screenpage = ScreensaverPage(driver)
    #screenpage.screensaver_button().click()
    #driver.close()

def test_navigate_articledashboard(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    #articlepage = ArticlesPage(driver)
    #time.sleep(3)
    #articlepage.return_article_button().click()
    #driver.close()

def test_login_page_correctpassword(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    loginpage=LoginPage(driver)
    loginpage.return_login_button().click()
    loginpage.return_login_password().click()
    loginpage.return_login_keyboard().click()
    loginpage.return_set_password().send_keys(123)
    loginpage.return_login_check1().click()
    loginpage.return_login_check2().click()
    #driver.close()

def test_login_page_incorrectpassword(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    loginpage=LoginPage(driver)
    loginpage.return_login_button().click()
    loginpage.return_login_password().click()
    loginpage.return_login_keyboard().click()
    loginpage.return_set_password().send_keys(1234)
    loginpage.return_login_check1().click()
    loginpage.return_login_check2().click()
    time.sleep(5)
    loginpage.return_incorrect_password().click()
    #invoke virtual keyboard again
    loginpage.return_login_password().click()
    loginpage.return_login_keyboard().click()
    loginpage.return_set_password().send_keys(123)
    loginpage.return_login_check1().click()
    loginpage.return_login_check2().click()
    #driver.close()

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
    #settingspage.settings_button1().click()
    #driver.close()


def test_monitoring_navigate_alltabs_monitoringtab(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    searchpage=MonitoringPage(driver)
    time.sleep(5)
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
    #driver.close()

# This test compares the header titles for Event logs Tab under monitoring dashboard
def test_Monitoring_Event_log(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    # Navigate to Article Dashboard
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    time.sleep(3)
    monitoring_page= MonitoringPage(driver)
    time.sleep(1)
    monitoring_page.return_search_button().click()
    time.sleep(1)
    monitoring_page.return_event_button().click()
    time.sleep(3)
    assert monitoring_page.return_event_log_title().text == "Event\nTimestamp"
    assert monitoring_page.return_event_log_maintitle().text == "Article 1 Position-1\nundo\nrefresh"
    monitoring_page.return_event_arrow().click()
    monitoring_page.return_event_run_inhibit().click()
    #driver.close()


# This test compares the header titles for compare monitoring dashboard
def test_compare_header(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(50)
    # Navigate to Article Dashboard
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    time.sleep(5)
    monitoring_page = MonitoringPage(driver)
    time.sleep(1)
    monitoring_page.return_search_button().click()
    time.sleep(1)
    assert monitoring_page.return_compare_header().text == "1\nCount alarm 0.00 Eff.%"
    assert monitoring_page.return_compare_header_article2().text == "Article 1"
    # Last 3 values of the Grid
    assert monitoring_page.return_compare_lastcell1().text == "05"
    assert monitoring_page.return_compare_lastcell2().text == "06"
    assert monitoring_page.return_compare_lastcell3().text == "07"
    #driver.close()

def test_monitoring_bad_positions(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    searchpage = MonitoringPage(driver)
    time.sleep(5)
    searchpage.return_search_button().click()
    searchpage.return_bad_positions().click()
    time.sleep(5)
    searchpage.return_bad_position_cv().click()
    #driver.close()

def test_edit_article(setup):
    driver = setup
    driver.get(TestLogin.baseURL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    screenpage = ScreensaverPage(driver)
    screenpage.screensaver_button().click()
    time.sleep(5)
    loginpage=LoginPage(driver)
    loginpage.return_login_button().click()
    loginpage.return_login_password().click()
    loginpage.return_login_keyboard().click()
    loginpage.return_set_password().send_keys(123)
    loginpage.return_login_check1().click()
    loginpage.return_login_check2().click()
    articlepage= ArticlesPage(driver)
    time.sleep(5)
    articlepage.return_articles_main_button().click()
    time.sleep(5)
    articlepage.return_articles_edit_article_lower().click()
    articlepage.return_articles_slider_button().click()
    articlepage.return_articles_save_changes().click()



