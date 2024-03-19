import pytest
from selenium import webdriver
#This is a conf file2

@pytest.fixture()
def setup(request):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver





