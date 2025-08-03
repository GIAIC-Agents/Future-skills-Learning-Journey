# 🌐 Step 02 – Open a Website URL using `.get()`

In this step, we will learn how to open a website like Google using Selenium’s `.get()` method.

---

## 🔍 What You Learn

- How to use `.get()` method to navigate to a website.
- This is used in almost every Selenium script.

---

## 🧠 Key Concepts

- `.get("https://www.google.com")` tells the browser to open a specific URL.
- Must be used **after** initializing the browser driver.

---

## 🔁 Alternatives

| Method                | Description                      |
|----------------------|----------------------------------|
| `.get(url)`          | Loads the page in the current tab |
| `.navigate().to(url)`| Only in Java Selenium (not Python) |

---


🔁 Alternatives
Option	Use Case
driver.get(url)	Loads the given web page (Python)
driver.navigate().to(url)	Used in Java Selenium only
driver.execute_script("window.location = 'https://...'")	JS redirect inside Selenium

⚠️ Warnings & Notes
Make sure the URL is valid and active.

If you're offline or have a slow connection, page load may hang.

Some sites may block bots — in such cases, you may need to set headers or use Selenium stealth options later.

✅ Output
After running this code:

A Chrome window opens

It loads https://www.google.com

You can now perform actions like search, inspect elements, etc.

🧯 Common Error
cpp
Copy
Edit
selenium.common.exceptions.WebDriverException: Message: unknown error: net::ERR_NAME_NOT_RESOLVED
📌 This means your internet is off or URL is invalid.