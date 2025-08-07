# 🚀 Web Automation: Scroll a Website using Selenium & Undetected ChromeDriver

This Python script demonstrates how to **automate a browser** using `undetected_chromedriver` (UC) and `Selenium`.  
It opens a scrollable website, waits for the content to load, scrolls down by 500 pixels, and then exits after a pause.

---

## 🧠 What You'll Learn

- How to use `undetected_chromedriver` to avoid bot detection  
- How to open a browser and navigate to a website using Selenium  
- How to scroll down a webpage programmatically  
- How to implement wait times to observe actions  
- How to cleanly close the browser  

---

## 📦 Requirements

Before running the script, install the following Python packages:

```bash
pip install selenium undetected-chromedriver

```
---

## 🧾 Script Breakdown
```
### ✅ Step 1: Import Libraries

from selenium import webdriver
import undetected_chromedriver as uc
import time
These are required libraries:

selenium: Controls the browser.

undetected_chromedriver: Bypasses bot detection used by websites.

time: Adds delays to simulate human interaction.
```

### ✅ Step 2: Launch Chrome Browser (Undetected)
```
driver = uc.Chrome()
This launches a Chrome browser in a way that helps bypass bot detection systems.
It’s commonly used on sites that block Selenium-based bots.
```
### ✅ Step 3: Visit a Scrollable Website
```
driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
This navigates to the Wikipedia page about Python, which is long enough to scroll.
```
### ✅ Step 4: Wait for Page to Load
```
time.sleep(10)
Waits 10 seconds to allow full page load. Adjust if your internet is slower/faster.
```
### ✅ Step 5: Scroll Down
```
driver.execute_script("window.scrollBy(0, 500)")
Scrolls down by 500 pixels. You can change 500 to any other number for deeper scrolls.
```
### ✅ Step 6: Wait to Observe Scroll
```
time.sleep(10)
Another pause to let the user see the scroll effect in the browser.
```
### ✅ Step 7: Close the Browser
```
driver.quit()
Ends the session and closes the browser window.
```
---


### 📸 Demo Preview (Steps Overview)


🚀 Launch Undetected Chrome

🌐 Open Wikipedia (Python Page)

🕒 Wait 10 seconds

🔽 Scroll down 500px

🕒 Wait again

❌ Close browser

---

### 📌 Notes

undetected_chromedriver is used when websites block bots based on browser automation detection.

Always use time delays responsibly. Overloading websites with rapid requests may lead to IP bans.

For dynamic or JavaScript-heavy pages, consider using explicit waits (WebDriverWait) instead of time.sleep.


---
### 📁 File Structure
bash
Copy
Edit
scroll_script.py       # Your main Python script  
README.md              # This documentation file  


---

## 📚 Useful Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [undetected-chromedriver GitHub](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
- [Wikipedia: Python (Language)](https://en.wikipedia.org/wiki/Python_(programming_language))


----
### 🔐 Disclaimer
This script is for educational and testing purposes only.
Do not use it to scrape or interact with websites without permission.

