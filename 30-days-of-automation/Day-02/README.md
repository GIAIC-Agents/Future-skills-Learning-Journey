# 📘 Day 02 – Selenium Baby Steps Summary
## 🚀 Overview:
In Day 02, we explored the foundational elements of interacting with web pages using Selenium. We moved beyond just opening a webpage, and learned how to locate elements, interact with forms, click buttons, capture screenshots, and intelligently wait for elements using different wait mechanisms.

### 🔍 Topics Covered:
1️⃣ Locating Elements by Different Selectors
We practiced using multiple strategies to locate elements on a webpage:
```python
find_element_by_name("username")

find_element_by_class_name("form-control")

find_element_by_xpath("//input[@id='email']")
```

📌 These allow us to identify and work with specific HTML elements.

----

### 2️⃣ Sending Text to Input Fields

Purpose:
We used .send_keys() method to automatically type into fields like:

```python
username_input.send_keys("myUsername")
```

### Purpose:

✅ Simulates real human typing into forms.

### 3️⃣ Clicking Buttons

Using .click() we triggered actions like form submissions, navigation, etc.

```python


submit_button.click()
```
 🖱️ Automates button interactions just like a user would.

### 4️⃣ Taking Screenshots
We learned how to take a screenshot of the entire page:
 ----

```pythom
driver.save_screenshot("snapshot.png")
```
## Purpose : 

📸 Helpful for debugging or saving test results.

### 5️⃣ Handling Waits in Selenium

Waits are crucial because websites take time to load elements. We covered two major types:

----

## 🔸 Implicit Wait

Sets a general wait time that applies to all elements.



### Syntax : 
```python
driver.implicitly_wait(10)
```

⏳ If element isn't immediately found, Selenium waits before throwing error.

## 🔸 Explicit Wait

We wait only for a specific condition using WebDriverWait.

### Syntax : 

```python
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "submit")))
```
----

⏱️ More flexible and accurate; used for elements that take longer to appear.


### 📌 Key Takeaway:
Day 02 was about interaction and timing. We went from passive automation (just opening pages) to active web automation — filling forms, waiting smartly, and capturing results.


### 🔮 What’s Next in Day 03?

Working with dropdowns

Checkbox & radio button selection

Handling alerts/popups

Browser navigation (forward/back)

Better error handling with try/except
