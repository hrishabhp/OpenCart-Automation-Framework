from selenium.webdriver.common.by import By

class LoginPage:
    # --- Locators ---
    lnk_myaccount_xpath = "//span[text()='My Account']"
    lnk_login_linktext = "Login"
    txt_email_id = "input-email"
    txt_password_id = "input-password"
    btn_login_xpath = "//input[@value='Login']"
    lnk_logout_linktext = "Logout"

    # --- Constructor ---
    def __init__(self, driver):
        self.driver = driver

    # --- Action Methods ---
    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()

    def clickLoginLink(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_login_linktext).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).clear()
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_logout_linktext).click()