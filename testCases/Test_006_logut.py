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
from pageObjects.signOut_pageObject import SignOut


class Test_006_logOut():

    baseURL = ReadConfig.getURL()
    log = LogGen.loggen()
    rand = RandomGen()

    @pytest.mark.smoke
    def test_logOut(self, setup):
        self.log.info('************* Test_006 *************')
        self.log.info('************* Verifying Logout *************')

        self.driver = setup
        self.driver.get(self.baseURL)

        signIn = SignIn(self.driver)
        test2 = TestTwo()
        signUp_obj = SignUp(self.driver)

        signUp_obj.signUp()
        signIn.email_signIn(test2.email)
        signIn.password_signIn(test2.password)
        signIn.signIn_btn()

        signOut_obj = SignOut(self.driver)
        signOut_obj.signOut()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "Sign in" in self.msg:
            assert True
            self.driver.close()
            self.log.info('************* Logout test is PASSED *************')
            self.log.info('- - - - - - - - - -')
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                     r'/Screenshoots/Test_006_logOut',
                                                     self.rand.random_generator(size=2,
                                                                                chars=string.ascii_lowercase + string.digits) + '_logOut_failed.png'))
            self.driver.close()
            self.log.error('************* Logout test is FAILED *************')
            self.log.info('- - - - - - - - - -')
            assert False