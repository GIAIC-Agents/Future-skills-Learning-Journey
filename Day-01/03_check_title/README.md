# 📑 Step 03 – Check Page Title with `.title`

This step focuses on getting the current page's title using Selenium’s `.title` attribute. It’s commonly used to verify if the correct page has loaded.

---

## 🔍 What You Learn

- How to extract the title of any web page.
- Title checking is a common method for test validation.

---

## 🧠 Key Concepts

- `driver.title` is a property, not a method.
- It returns a string — the current document’s title.
- It can be used for **assertions** in testing frameworks like `unittest` or `pytest`.

---

## 🧪 Example Output

If you open Google:


---

## 🔁 Alternatives

| Option | Description |
|--------|-------------|
| `driver.title` | Standard method in Selenium (Python) |
| `driver.execute_script("return document.title")` | JavaScript alternative (if needed) |

```python
# JS-based title check (not recommended for beginners):
title = driver.execute_script("return document.title")

⚠️ Common Errors
Using driver.title() (with brackets) will throw an error — it’s a property, not a method.

Title might be empty for pages that use dynamic JavaScript rendering.

🧯 Troubleshooting
If you get '' as title:

Check if the page is still loading.

Try adding a small delay using time.sleep(2) or WebDriverWait.


✅ Use Cases

Verifying if login/signup pages are loaded correctly.

Debugging redirects.

Logging or reporting current test steps.

