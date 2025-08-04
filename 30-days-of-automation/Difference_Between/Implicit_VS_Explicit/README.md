# 📅 Day 02 – Interacting with Web Elements and Understanding Waits in Selenium
## Difference Between Implicit & Explicit Waits
---

## 📌 What We Covered Today

### ✅ Step-by-Step Summary:
1. Navigated to a test website using `webdriver.Chrome()`.
2. Located and filled text fields using `send_keys()`.
3. Clicked a button using `.click()`.
4. Printed response text to verify success.
5. Learned about **Waits** in Selenium (Implicit vs. Explicit).

---

## ⏱️ Understanding Selenium Waits

In real-world websites, elements may take time to appear due to loading delays or network speed. Selenium provides two primary types of waits to handle these cases:

---

### 1️⃣ **Implicit Wait**

An implicit wait tells WebDriver to wait for a certain amount of time **while finding elements**.

#### 🔹 Syntax:
```python
driver.implicitly_wait(10)

```
---

🔸 How It Works:

Applies globally to all find_element() calls.

Selenium will wait up to 10 seconds before throwing a "NoSuchElementException".

If the element appears earlier, it continues immediately.

### ✅ Use When:
Your elements usually appear in a few seconds.

You want a simple, global timeout.

----

## 2️⃣ Explicit Wait
An explicit wait lets you wait for a specific condition before proceeding.

### 🔹 Syntax:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "submit")))
```

----

### 🔸 How It Works:

Waits up to 10 seconds for the condition to be true.

You can wait for:

Presence of element

Visibility

Clickability

URL or title change

Much more controlled and powerful than implicit wait.



## ✅ Use When:

You're interacting with dynamic elements (e.g., pop-ups, AJAX data).

You want to wait only for specific elements or events.

### 🔍 Key Differences

Feature	Implicit Wait	Explicit Wait
Scope	Global (applies to all finds)	Local (applies to specific element)
Custom Conditions	❌ Not Supported	✅ Fully Supported
Use Cases	Basic sites with predictable load	Dynamic pages with AJAX, JS delays
Flexibility	Low	High

### 💡 Pro Tip
🔸 Do not mix Implicit and Explicit waits too much — it can lead to unpredictable results and timing issues.






