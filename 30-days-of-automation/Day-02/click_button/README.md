# Step 05 – Clicking Buttons in Selenium

This step teaches how to interact with clickable elements, such as buttons and form submissions.

---

## 🖱️ Clicking a Button

Use `.click()` to simulate a user pressing a button:

```python
element = driver.find_element(By.ID, "submit")
element.click()

```
The method works for any clickable element, including:

<button>

<input type="submit">

<a> tags with JavaScript events


## ✅ Verifying Button Actions

After clicking, you can verify page content to confirm the action worked. For example:


text = driver.find_element(By.TAG_NAME, "h1").text
print(text)



## 🧪 What This Script Does

Opens the browser and goes to the login page.

Fills in valid username and password.

Clicks the login button.

Waits for the page to load.

Extracts text from the result page to confirm success.

Closes the browser.



## 🔍 Troubleshooting Tip

If .click() doesn’t work:

Ensure the element is visible.

Try driver.execute_script("arguments[0].click();", element) for tricky buttons.

Check if the page uses JavaScript for custom clicks.

## 💡 Real-world usage:

 Clicking buttons is central in automation—whether it's submitting forms, confirming modals, or navigating through steps.

