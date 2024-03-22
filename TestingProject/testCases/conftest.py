import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

#This is a conf file2
baseURL = "http://13.68.159.147/"
@pytest.fixture()
def log_on_failure(request):
    yield
    item=request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name='Failed test', attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture()
def setup(request):
    global driver
    options = webdriver.ChromeOptions()
    #options.headless = True
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver





