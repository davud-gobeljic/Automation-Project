import pytest
from Utilities.readProperties import ReadConfig
from Utilities.logger import LogGen
from pageObjects.signUp_pageObject import SignUp
from pageObjects.randomGenerator import RandomGen
from selenium.webdriver.common.by import By
from pageObjects.shoppingDresses_pageObject import Shopping_dresses as SD


class Test_004_shopping():

    baseURL = ReadConfig.getURL()
    log = LogGen.loggen()
    rand = RandomGen()

    size = "l"
    dressColor = "blue"

    @pytest.mark.smoke
    def test_004(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.sd = SD(self.driver)
        self.sd.dresses_menu_hover()
        self.sd.price_slider()
        self.sd.chooseSize(self.size)
        self.sd.chooseColor(self.dressColor)
        self.sd.hoverImage()

