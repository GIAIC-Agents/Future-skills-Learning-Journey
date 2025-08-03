## Difference Between quit() and close() : 


## ✅ driver.close():
Closes only the current browser tab or window that the driver is focused on.

If your automation opened multiple tabs/windows, close() will only shut the one currently active.

The WebDriver session remains active unless it was the last window.

## Example:

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

driver.close()  # Only this tab closes



## ✅ driver.quit():

Closes all browser windows/tabs that were opened by the WebDriver.

Ends the entire WebDriver session, releasing memory and system resources.

After quit(), the driver object is unusable.

## Example:

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

driver.quit()  # All tabs and browser instances close



## 🔍 Summary:

Method	Closes What?	Ends WebDriver Session?

close()	Current tab/window only	❌ No
quit()	All tabs/windows	✅ Yes

## 💡 Best Practice:
U
se close() when you’re done with a single tab.

Use quit() when your test is fully complete and you want to clean up everything.