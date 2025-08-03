# 🧪 Step 01 – Open Chrome Browser with Selenium

In this step, we are simply opening a new Chrome browser window using the `webdriver.Chrome()` method from Selenium.

---

## 🔍 What You Learn

- How to **import and use Selenium's webdriver**
- How to **launch Chrome browser**
- This is the **foundation** for all future automation tasks

---

## 🧠 Key Concepts

- `webdriver.Chrome()` is a Selenium constructor that starts a new Chrome session.
- You must have the **Chrome browser** and **ChromeDriver** installed and properly added to your system's PATH.

---

## 🔁 Alternatives

| Alternative | Description |
|------------|-------------|
| `webdriver.Firefox()` | Opens Firefox browser (needs geckodriver) |
| `webdriver.Edge()`    | Opens Microsoft Edge (needs msedgedriver) |
| `webdriver.Safari()`  | For macOS only |

```python
# Example for Firefox:
from selenium import webdriver
driver = webdriver.Firefox()
