import os
import string
import random
import pytest
from Utilities.readProperties import ReadConfig
from Utilities.logger import LogGen
from pageObjects.randomGenerator import RandomGen
from selenium.webdriver.common.by import By
from pageObjects.signIn_pageObject import SignIn
from pageObjects.signUp_pageObject import SignUp
from testCases.Test_002_signUp import Test_002_signUp as TestTwo


class Test_003_signIn():

    baseURL = ReadConfig.getURL()
    log = LogGen.loggen()
    rand = RandomGen()

    @pytest.mark.smoke
    def test_signIn(self, setup):
        self.log.info('************* Test_003 *************')
        self.log.info('************* Verifying SignIn *************')

        self.driver = setup
        self.driver.get(self.baseURL)
        self.signUp = SignUp(self.driver)
        self.signUp.signUp()
        self.testTwo = TestTwo()

        self.signIn = SignIn(self.driver)

        self.signIn.email_signIn(self.testTwo.email)
        self.signIn.password_signIn(self.testTwo.password)
        self.signIn.signIn_btn()

        myAccount = "MY ACCOUNT"

        h1_text = self.driver.find_element(By.TAG_NAME, "h1").text
        print(h1_text)

        if myAccount == h1_text:
            assert True
            self.driver.close()
            self.log.info('************* Sign In test is PASSED *************')
            self.log.info('- - - - - - - - - -')
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                     r'/Screenshoots/Test_003_signIn',
                                                     self.rand.random_generator(size=2,
                                                                                chars=string.ascii_lowercase + string.digits) + '_signIn_failed.png'))
            self.driver.close()
            self.log.error('************* Sign In test is FAILED *************')
            self.log.info('- - - - - - - - - -')
            assert False