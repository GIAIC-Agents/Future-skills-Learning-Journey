from selenium import webdriver

# Launch the Chrome browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Print the current URL
print("Current URL:", driver.current_url)

# Close the browser
driver.quit()
