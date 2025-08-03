# 🌍 Step 04 – Get Current URL with `.current_url`

This step shows how to get the actual URL currently loaded in the browser using Selenium's `.current_url` property. It’s helpful for debugging and redirection tracking.

---

## 🔍 What You Learn

- How to get the **exact URL** loaded in the browser tab.
- Useful when websites redirect after login or button clicks.

---

## 🧠 Key Concepts

- `.current_url` returns the URL of the currently loaded page.
- It’s useful to confirm you’ve landed on the correct page — especially when redirections happen (e.g., login success).

---

## 🧪 Example Output

If you open Google:

Current URL: https://www.google.com/

---

## 🔁 Alternatives

| Option | Description |
|--------|-------------|
| `driver.current_url` | Official Selenium way |
| `driver.execute_script("return window.location.href")` | JavaScript alternative |

```python
# JS-based URL check (not beginner-friendly)
url = driver.execute_script("return window.location.href")
⚠️ Common Errors
If .get() failed (site didn’t load), current_url might be wrong or blank.

May return redirect URLs (e.g., https://example.com/login?next=/home).

✅ Use Cases
Confirm redirections (e.g., after login, logout, form submission).

URL-based test verification.

Useful in scraping or automated browser flows.

💡 Tips
You can compare the URL in assertions:

python
Copy
Edit
assert \"login\" in driver.current_url
