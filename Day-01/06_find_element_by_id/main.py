from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open Google's homepage
driver.get("https://www.google.com")

# Wait for page to load
time.sleep(2)

# Locate the search input using its ID
search_box = driver.find_element(By.ID, "APjFqb")

# Print the tag name of the located element
print("Element tag name:", search_box.tag_name)

# Close browser
driver.quit()
