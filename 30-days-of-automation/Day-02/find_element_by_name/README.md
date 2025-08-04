# Step 01 – Find Element by Name

### 🔍 Feature
We used the `find_element(By.NAME, "q")` method to locate the Google search bar by its name attribute (`q`). Then we sent text using `.send_keys()`.

### 💡 Key Concepts
- `By.NAME` is useful when an input or form field has a unique `name` attribute.
- `.send_keys("text")` simulates typing into an input field.

### 🆚 Alternative Approaches
- You can use `By.ID` or `By.CLASS_NAME` if the element has those attributes.
- `By.XPATH` is more flexible but a bit complex.

### ✅ Real-World Usage
Logging into a website, searching on Google, or filling forms.

---

⏭️ **Next**: We'll use `find_element_by_class_name`.
