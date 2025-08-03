# 🚀 Selenium Day 01 – Baby Steps in Web Automation

Welcome to **Day 01** of my Selenium learning journey!  
In this session, I explored the **first 6 baby steps** that lay the foundation for browser automation using Selenium with Python 🐍 and Chrome 🌐.

Whether you're a complete beginner or just brushing up, these basic building blocks will set you on the right path toward mastering Selenium.

---

## 📚 What I Learned Today

Here’s a breakdown of what each script does in Day 01:

---

### 🟢 Step 01 – Open Browser
**Filename:** `01_open_browser.py`  
**Goal:** Launches a new Chrome browser window using `webdriver.Chrome()`  
🔧 This is the very first step of any automation — without this, nothing happens!

---

### 🌐 Step 02 – Open URL
**Filename:** `02_open_url.py`  
**Goal:** Opens a specific website (e.g., Google) using `.get("https://...")`  
🌍 Teaches how to load a web page — must-know for all future tasks.

---

### 📑 Step 03 – Check Page Title
**Filename:** `03_check_title.py`  
**Goal:** Prints the title of the loaded page using `.title`  
🔍 Useful for verifying whether the page loaded is correct.

---

### 🔗 Step 04 – Get Current URL
**Filename:** `04_get_current_url.py`  
**Goal:** Retrieves the current page’s URL using `.current_url`  
🧭 Helps in tracking redirects and ensuring you're on the expected page.

---

### ❌ Step 05 – Close Browser Tab
**Filename:** `05_close_browser.py`  
**Goal:** Closes the **currently active** browser tab using `.close()`  
🪟 Only closes the focused tab — not the entire browser session.

---

### 🧠 Step 06 – Find Element by ID
**Filename:** `06_find_element_by_id.py`  
**Goal:** Locates a web element using `By.ID`  
🔎 The first step toward interacting with web forms, buttons, inputs, etc.

---

## 🛠 Tools Used

- **Language:** Python 3.x  
- **Automation Library:** Selenium  
- **Browser:** Google Chrome  
- **Driver:** ChromeDriver  

### 📦 Installation
```bash
pip install selenium

## Folder Structure

selenium-day01/
├── 01_open_browser/
│   ├── script.py
│   └── README.md
├── 02_open_url/
├── 03_check_title/
├── 04_get_current_url/
├── 05_close_browser/
├── 06_find_element_by_id/
└── README.md  <-- This file


💡 Why This Matters
Each small script may seem simple, but together they form the base for:

Web scraping

Automated form submissions

UI testing

Bot development

🔜 What’s Coming in Day 02?
📅 In the next session:

More element-finding methods (By.NAME, By.CLASS_NAME, By.XPATH)

Typing into fields

Clicking buttons

Taking screenshots

Using waits (implicit & explicit)

🙌 Made with focus by Hafiz Muneeb & Miss Rubina
This is part of my self-study and practice. Feel free to use or fork this repo if you're learning Selenium too!