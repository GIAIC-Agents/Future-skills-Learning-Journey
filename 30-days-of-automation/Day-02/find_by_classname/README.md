# Step 02 – Find Element by Class Name

### 🔍 Feature
We used the `.find_element(By.CLASS_NAME, "form-control")` to locate the input box.

### 💡 Key Concepts
- `By.CLASS_NAME` finds the **first** element matching that class.
- Many websites use **Bootstrap classes** like `form-control`, `btn`, etc.

### ⚠️ Caution
- If multiple elements have the same class, you might need `.find_elements()` or a more specific locator like XPath or CSS Selector.

### ✅ Real-World Usage
Useful when you know the class name of input fields, buttons, or form sections.

---

⏭️ **Next**: We’ll use `find_element_by_xpath` and understand XPath basics.
