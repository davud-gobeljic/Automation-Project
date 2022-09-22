import os
import string
from Utilities.readProperties import ReadConfig
from Utilities.logger import LogGen
from pageObjects.randomGenerator import RandomGen

class Test_001_homePage_title():

    baseURL = ReadConfig.getURL()
    log = LogGen.loggen()
    rand = RandomGen()
    pageTitle = 'My Store'


    def test_homePage_title(self, setup):
        self.log.info('************* Test_001 *************')
        self.log.info('************* Verifying Home Page Title *************')
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == self.pageTitle:
            assert True
            self.driver.close()
            self.log.info('************* Home Page title test is PASSED *************')
            self.log.info('- - - - - - - - - -')
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                     r'/Screenshoots/Test_001_homePage_title',
                                                     self.rand.random_generator(size=2,
                                                                                chars=string.ascii_lowercase + string.digits) + '_homePage_title_failed.png'))
            self.driver.close()
            self.log.error('************* Home Page title test is FAILED *************')
            self.log.info('- - - - - - - - - -')
            assert False