from selenium import webdriver

# Launch the Chrome browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Print the title of the page
print("Page Title:", driver.title)

# Close the browser
driver.quit()
