from selenium import webdriver
import undetected_chromedriver as uc
import time

# Step 1: Open browser
driver = uc.Chrome()

# Step 2: Go to a scrollable website
driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

# Step 3: Wait for the page to load
time.sleep(10)

# Step 4: Scroll down by 500 pixels
driver.execute_script("window.scrollBy(0, 500)")

# Step 5: Wait to see the scroll
time.sleep(10)

# Step 6: Close browser
driver.quit()
