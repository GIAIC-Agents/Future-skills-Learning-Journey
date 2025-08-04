from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

# Enter login details
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")

# Click the Login button
login_button = driver.find_element(By.ID, "submit")
login_button.click()

# Wait for result page to load
time.sleep(2)

# Optional: Verify if login was successful
success_message = driver.find_element(By.TAG_NAME, "h1").text
print("Login Result:", success_message)

# Close browser
driver.quit()
