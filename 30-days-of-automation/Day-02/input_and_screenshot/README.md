# Step 04 – Send Text to Input Fields & Take Screenshot

In this step, we interact with input fields and learn how to capture screenshots of the browser state.

---

## ✍️ Filling Input Fields

To **send text** to a text field or input box, we use:

```python
element.send_keys("your text here")


```
---

## Example:

driver.find_element(By.ID, "username").send_keys("student")

This simulates a human typing into the input box.

## 📸 Taking Screenshots

Screenshots are useful for debugging or reporting automation results.

driver.save_screenshot("filename.png")
This saves a PNG image of the current state of the browser.

## 🔁 Workflow in this Script

Launch browser and open the login page.

Fill in username and password.

Take screenshot named before_login.png.

Click the login button.

Wait 2 seconds.

Take screenshot named after_login.png.

Close the browser.

## ✅ Why It Matters?

Screenshots show proof that your automation ran correctly.

Sending keys is used in nearly every web automation project, from login forms to data scraping.

You can combine screenshots with test logs or reports later in advanced automation.

