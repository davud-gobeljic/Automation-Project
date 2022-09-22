from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


class ShoppingComplete():
    bestSellers_xpath = "//a[normalize-space()='Best Sellers']"
    blouse_xpath = "(//img[@title='Blouse'])[2]"
    more_xpath = "(//span[contains(text(),'More')])[10]"
    quantity_id = "quantity_wanted"
    select_id = "group_1"
    addToCart_id = "add_to_cart"
    proceedToChekcout_xpath = "//span[normalize-space()='Proceed to checkout']"
    proceedToChekcout2_xpath = "//a[@class='button btn btn-default standard-checkout button-medium']"
    input_email_id = "email"
    input_password_id = "passwd"
    submit_login_id = "SubmitLogin"
    proceedToChekcout3_name = "processAddress"
    agreeWithTerms_radio_id = "cgv"
    proceedToChekcout4_name = "processCarrier"
    confirmOrder_xpath = "//button[@class='button btn btn-default button-medium']"

    def __init__(self, driver):
        self.driver = driver

    def bestsellers(self):
        self.driver.find_element(By.XPATH, self.bestSellers_xpath).click()

    def blouse(self):
        blouse = self.driver.find_element(By.XPATH, self.blouse_xpath)
        ac = ActionChains(self.driver)
        ac.move_to_element(blouse).perform()
        more = self.driver.find_element(By.XPATH, self.more_xpath)
        more.click()

    def quantity(self, quantity):
        self.driver.find_element(By.ID, self.quantity_id).clear()
        self.driver.find_element(By.ID, self.quantity_id).send_keys(quantity)

    def sizeSelect(self, size):
        sel = Select(self.driver.find_element(By.ID, self.select_id))
        sel.select_by_visible_text(size)

    def addToCartBTN(self):
        self.driver.find_element(By.ID, self.addToCart_id).click()

    def proceedToCheckoutBTN(self):
        self.driver.find_element(By.XPATH, self.proceedToChekcout_xpath).click()

    def proceedToCheckoutBTN2(self):
        self.driver.find_element(By.XPATH, self.proceedToChekcout2_xpath).click()

    def signIn(self, email, password):
        self.driver.find_element(By.ID, self.input_email_id).send_keys(email)
        self.driver.find_element(By.ID, self.input_password_id).send_keys(password)
        self.driver.find_element(By.ID, self.submit_login_id).click()

    def proceedToCheckoutBTN3(self):
        self.driver.find_element(By.NAME, self.proceedToChekcout3_name).click()

    def agreeTermsandCond(self):
        self.driver.find_element(By.ID, self.agreeWithTerms_radio_id).click()

    def proceedToCheckoutBTN4(self):
        self.driver.find_element(By.NAME, self.proceedToChekcout4_name).click()

    def payWithBank(self):
        self.driver.find_element(By.CLASS_NAME, "bankwire").click()

    def orderConfirmBTN(self):
        self.driver.find_element(By.XPATH, self.confirmOrder_xpath).click()

