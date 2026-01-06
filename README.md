# Hybrid E-Commerce Test Automation Framework – OpenCart

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green.svg)
![Pytest](https://img.shields.io/badge/Pytest-Framework-orange.svg)

## 📌 Project Overview
This is a scalable **Hybrid Test Automation Framework** built to automate the end-to-end (E2E) flows of an E-Commerce application. The project targets the **OpenCart** platform (via TutorialsNinja) to validate critical business flows like User Login and Account Management.

The framework implements the **Page Object Model (POM)** design pattern to separate test logic from page objects, ensuring high maintainability. It also features **Data-Driven Testing (DDT)** using Excel to validate multiple user credentials efficiently.

## 🛠 Tech Stack
* **Language:** Python
* **Automation Tool:** Selenium WebDriver (v4.x)
* **Testing Framework:** Pytest
* **Design Pattern:** Page Object Model (POM)
* **Data Source:** Excel (OpenPyXL)
* **Reporting:** Pytest-HTML Reports

## 📂 Framework Architecture
The project follows a standard modular structure:

```text
OpenCart-Automation-Framework/
├── configurations/    # Config.ini (Common URLs & Credentials)
├── logs/              # Automation Logs (Generated during run)
├── pageObjects/       # Page Classes (Locators & Actions)
├── reports/           # HTML Test Reports (Screenshots & Results)
├── testCases/         # Test Scripts (Pytest files)
├── testData/          # Excel Files (LoginData.xlsx)
├── utilities/         # Common Utilities (ExcelReader, ConfigReader)
├── requirements.txt   # Project Dependencies
└── README.md          # Project Documentation
```

🚀 Key Features

1. Hybrid Structure: Combines Modular (POM) and Data-Driven approaches.
2. Data-Driven Testing: Reads multiple test datasets from testData/LoginData.xlsx.
3. Dynamic Waits: Implements Selenium Implicit Waits for stability.
4. Reporting: Generates detailed HTML reports automatically.
5. Cross-Browser Support: Configurable via conftest.py (Chrome default).

🧪 How to Run the Tests
1. Install Dependencies
```
pip install -r requirements.txt
```
2. Run All Tests
```
pytest -v -s testCases/
```
3. Run Data-Driven Login Test
```
pytest -v -s testCases/test_login_ddt.py
```
4. Generate HTML Report
```
pytest -v -s --html=reports/report.html testCases/test_login_ddt.py
```

👤 Author
```
HRISHABH CHANDRA PAL
```

LinkedIn: linkedin.com/in/hrishabhchandrapal

GitHub: github.com/hrishabhp
