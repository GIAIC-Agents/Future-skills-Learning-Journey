# ❌ Step 05 – Close the Browser Tab using `.close()`

In this step, you'll learn how to close the **current browser tab** using Selenium’s `.close()` method.

---

## 🔍 What You Learn

- The difference between `.close()` and `.quit()`
- How to close only the active tab and keep the rest (if any) open

---

## 🧠 Key Concepts

- `driver.close()` will close the **currently focused tab** only.
- If there’s only one tab, it will close the entire browser window.
- Selenium session still remains active until you use `.quit()`.

---

## 🧪 Example Output

- Chrome browser opens → Google loads → waits 3 seconds → tab closes

---

## 🔁 Alternatives

| Method         | Description                                   |
|----------------|-----------------------------------------------|
| `driver.close()` | Closes the active tab (but driver remains alive) |
| `driver.quit()`  | Closes the whole browser & ends WebDriver session |

---

## ⚠️ Common Mistakes

- Using `.close()` and expecting the whole browser to shut down (use `.quit()` for that).
- Forgetting to use `time.sleep()` or waits and browser closes before you see anything.

---

## ✅ When to Use `.close()`

- When you're working with **multiple tabs** and want to close one.
- After completing a task in a temporary popup tab.




---

## 💡 Tip

If you want to confirm tab is closed and script ends cleanly, add:

```python
print(\"Tab closed successfully!\")
