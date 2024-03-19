import pytest
from selenium import webdriver



@pytest.fixture()
def login():
        options = webdriver.ChromeOptions()
        options.headless(True)
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(options=options)
        browser.get("http://13.68.159.147/")
        browser.maximize_window()
        browser.implicitly_wait(100)
        browser.find_element_by_xpath("/html/body/app-root/app-screen-saver/div[2]/div/div/div/div[1]/div[1]").click()
        text_num = browser.find_element_by_xpath(
                "/html/body/app-root/app-shell/div[2]/div/app-machine-dashboard/div/app-machine-efficiency[1]/loe-dashboard-tile/div/div[2]/div/span").text
        print(text_num)
        assert text_num == "48.0%"


def test_click(login):
      pass

