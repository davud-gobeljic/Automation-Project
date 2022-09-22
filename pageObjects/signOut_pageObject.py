from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SignOut():

    signUp_xpath = "//a[@title='Log me out']"

    def __init__(self, driver):
        self.driver = driver

    def signOut(self):
        self.driver.find_element(By.XPATH, self.signUp_xpath).click()