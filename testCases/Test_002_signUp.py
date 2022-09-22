import os
import string
import pytest
from Utilities.readProperties import ReadConfig
from Utilities.logger import LogGen
from pageObjects.signUp_pageObject import SignUp
from pageObjects.randomGenerator import RandomGen
from selenium.webdriver.common.by import By


class Test_002_signUp():

    baseURL = ReadConfig.getURL()
    log = LogGen.loggen()
    rand = RandomGen()

    firstname = "John"
    lastname = "Doe"
    email = "johniotya@gmail.com"
    female = "female"
    male = "male"
    dayOfBirth = "24"
    monthOfBirth = "8"
    yearOfBirth = "1990"
    password = "abcfftuoy"
    company = "Atlaass"
    address = "Oleg Gunar 412"
    city = "New Yor"
    state = "New York"
    postalCode = "71000"
    phone1 = "51251928"
    phone2 = "897851928"


    @pytest.mark.smoke
    def test_signUp(self, setup):
        self.log.info('************* Test_002 *************')
        self.log.info('************* Verifying SignUp *************')

        # Webdriver
        self.driver = setup
        self.driver.get(self.baseURL)

        # Instance od Sign class from pageObject
        self.signUp = SignUp(self.driver)
        self.signUp.signUp()

        self.signUp.setEmail(self.email)
        self.signUp.submitClick()

        self.signUp.chooseGender(self.female)
        self.signUp.setFirstName(self.firstname)
        self.signUp.setLastName(self.lastname)
        self.signUp.setPassword(self.password)
        self.signUp.setDateOfBirth(self.dayOfBirth, self.monthOfBirth, self.yearOfBirth)
        self.signUp.newsletter()
        self.signUp.receiveOffers()
        self.signUp.setCompany(self.company)
        self.signUp.setAddress(self.address)
        self.signUp.setAddress2("")
        self.signUp.setCity(self.city)
        self.signUp.setState(self.state)
        self.signUp.postalCode(self.postalCode)
        self.signUp.additionalInfo("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        self.signUp.setPhones(self.phone1, self.phone2)
        self.signUp.createAccount()

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text
        print(self.msg)

        account_msg = "Welcome to your account"

        # Validation
        if account_msg in self.msg:
            assert True
            self.driver.close()
            self.log.info('************* Sign up test is PASSED *************')
            self.log.info('- - - - - - - - - -')
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                     r'/Screenshoots/Test_002_signUp',
                                                     self.rand.random_generator(size=2,
                                                                                chars=string.ascii_lowercase + string.digits) + '_signUp_failed.png'))
            self.driver.close()
            self.log.error('************* Sign up test is FAILED *************')
            self.log.info('- - - - - - - - - -')
            assert False
