import os
import string
import pytest
from Utilities.readProperties import ReadConfig
from Utilities.logger import LogGen
from pageObjects.signUp_pageObject import SignUp
from pageObjects.randomGenerator import RandomGen
from selenium.webdriver.common.by import By
from pageObjects.shoppingDresses_pageObject import Shopping_dresses as SD
from pageObjects.shoppingComplete_pageObject import ShoppingComplete
from testCases.Test_002_signUp import Test_002_signUp
from pageObjects.signIn_pageObject import SignIn


class Test_005_shoppingComplete():

    baseURL = ReadConfig.getURL()
    log = LogGen.loggen()
    rand = RandomGen()
    test2 = Test_002_signUp()

    @pytest.mark.smoke
    def test_005(self, setup):
        self.log.info('************* Test_005 *************')
        self.log.info('************* Verifying Complete Shopping functionality *************')
        self.driver = setup
        self.driver.get(self.baseURL)

        self.sopCmpl = ShoppingComplete(self.driver)
        self.sopCmpl.bestsellers()
        self.sopCmpl.blouse()
        self.sopCmpl.quantity("5")
        self.sopCmpl.sizeSelect("M")
        self.sopCmpl.addToCartBTN()

        self.sopCmpl.proceedToCheckoutBTN()
        self.sopCmpl.proceedToCheckoutBTN2()

        self.sopCmpl.signIn("kitoooo@gmail.com","gdsogijsdo")
        self.sopCmpl.proceedToCheckoutBTN3()
        self.sopCmpl.agreeTermsandCond()
        self.sopCmpl.proceedToCheckoutBTN4()
        self.sopCmpl.payWithBank()
        self.sopCmpl.orderConfirmBTN()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        orderConfirm = "ORDER CONFIRMATION"

        if orderConfirm in self.msg:
            assert True
            self.driver.close()
            self.log.info('************* Shopping test 005 is PASSED *************')
            self.log.info('- - - - - - - - - -')
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                     r'/Screenshoots/Test_005_shoppingComplete',
                                                     self.rand.random_generator(size=2,
                                                                                chars=string.ascii_lowercase + string.digits) + '_ShoppingFailed_failed.png'))
            self.driver.close()
            self.log.error('************* Checkbox Textbox FAILED *************')
            self.log.info('- - - - - - - - - -')
            assert False