from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver = webdriver.Chrome()
driver.get("https://www.google.com")
search = driver.find_element(By.NAME , "q")
search.send_keys("Open AI")
search.submit()
time.sleep(10)
driver.quit()