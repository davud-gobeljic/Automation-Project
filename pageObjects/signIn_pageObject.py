from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class SignIn():

    inputEmail_id = "email"
    inputPassword_id = "passwd"
    signIn_btn_id = "SubmitLogin"

    def __init__(self, driver):
        self.driver = driver

    def email_signIn(self, email):
        self.driver.find_element(By.ID, self.inputEmail_id).send_keys(email)

    def password_signIn(self, password):
        self.driver.find_element(By.ID, self.inputPassword_id).send_keys(password)

    def signIn_btn(self):
        self.driver.find_element(By.ID, self.signIn_btn_id).click()



