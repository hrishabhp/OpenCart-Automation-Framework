import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By  # Needed for the check


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.lp.clickMyAccount()
        self.lp.clickLoginLink()

        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # --- VALIDATION LOGIC ---
        # We check if the "Logout" button is visible.
        # This proves the user is logged in.
        try:
            # The 'implicitly_wait' in conftest.py will make this wait up to 10s
            logout_btn = self.driver.find_element(By.LINK_TEXT, "Logout")

            if logout_btn.is_displayed():
                assert True
            else:
                assert False
        except:
            # If find_element fails (button not found), the test fails
            assert False
