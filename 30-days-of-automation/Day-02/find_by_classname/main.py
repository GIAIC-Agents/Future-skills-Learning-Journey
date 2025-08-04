from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
username = driver.find_element(By.CLASS_NAME , "form-control")
username.send_keys("student")

time.sleep(20)
driver.quit()