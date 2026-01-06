import pytest
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities import ExcelUtils
from selenium.webdriver.common.by import By


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".\\testData\\LoginData.xlsx"

    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in Excel:", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            # --- THE FIX IS HERE ---
            # If the excel row is empty (None), we skip it to avoid the error
            if self.user is None:
                continue
            # -----------------------

            self.lp.clickMyAccount()
            self.lp.clickLoginLink()
            self.lp.setEmail(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)

            target_page = False
            try:
                logout_btn = self.driver.find_element(By.LINK_TEXT, "Logout")
                target_page = logout_btn.is_displayed()
            except:
                target_page = False

            if target_page == True:  # Login Successful
                if self.exp == "Pass":
                    print(f"Row {r}: Login Success (Expected) -> PASS")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    print(f"Row {r}: Login Success (Not Expected) -> FAIL")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif target_page == False:  # Login Failed
                if self.exp == "Pass":
                    print(f"Row {r}: Login Failed (Expected Success) -> FAIL")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    print(f"Row {r}: Login Failed (Expected Failure) -> PASS")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            assert True
        else:
            assert False