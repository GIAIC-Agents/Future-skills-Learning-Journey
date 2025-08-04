from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
username = driver.find_element(By.XPATH , '//*[@id= "username"]')
username.send_keys("student")
password = driver.find_element(By.XPATH , '//*[@id= "password"]')
password.send_keys("Password123")
Login_Button = driver.find_element(By.XPATH , '//*[@id = "submit"]')
Login_Button.click()
time.sleep(10)
driver.quit()