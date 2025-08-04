# Step 03 – Find Element by XPath

### 🔍 Feature
XPath (XML Path Language) allows you to target elements precisely using their tag, attributes, hierarchy, etc.

### 🧠 Syntax Used
```python
driver.find_element(By.XPATH, '//*[@id="username"]')

📌 Explanation:
// → Search anywhere in the document.

* → Any tag (div, input, button, etc.)

@id="username" → Find element where id equals "username".

💡 Why XPath?
Helpful when:

Class names are reused.

No unique ID is present.

You want to select based on element hierarchy or text.

# ✅ Pro Tip
You can right-click an element in Chrome > Inspect > Right click again > Copy > Copy XPath