from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID , "password").send_keys("Password123")

driver.save_screenshot("before_login.png")

driver.find_element(By.ID, "submit").click()

driver.save_screenshot("After_login.png")

time.sleep(10)
driver.quit()

