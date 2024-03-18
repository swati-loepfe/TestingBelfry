
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://13.68.159.147/")
driver.maximize_window()
driver.implicitly_wait(100)

driver.find_element_by_xpath("/html/body/app-root/app-screen-saver/div[2]/div/div/div/div[1]/div[1]").click()

text_num= driver.find_element_by_xpath("/html/body/app-root/app-shell/div[2]/div/app-machine-dashboard/div/app-machine-efficiency[1]/loe-dashboard-tile/div/div[2]/div/span").text
#Login lock key
driver.find_element_by_xpath("/html/body/app-root/app-shell/div[1]/div[3]/div[1]/app-login/div").click()
#Input keyboard key
driver.find_element_by_xpath("//*[@id='cdk-dialog-0']/app-login-dialog/loe-dashboard-tile/div/div[2]/loe-input").click()
#Input password
driver.find_element_by_xpath("/html/body/app-root/loe-keyboard-loader/loe-keyboard/div[2]/input").send_keys(123)
driver.find_element_by_xpath("/html/body/app-root/loe-keyboard-loader/loe-keyboard/div[2]/div/div/div[5]/div[3]").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div/cdk-dialog-container/app-login-dialog/loe-dashboard-tile/div/div[2]/div/loe-button[2]/div/div/span").click()

#print(text_num)
#assert text_num == "48.0%"




