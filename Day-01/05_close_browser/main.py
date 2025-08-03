from selenium import webdriver
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# Wait for 3 seconds (just to visually confirm it's open)
time.sleep(3)

# Close the current tab
driver.close()
