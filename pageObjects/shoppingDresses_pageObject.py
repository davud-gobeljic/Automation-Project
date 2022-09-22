import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

class Shopping_dresses():

    dresses_menu_xpath = "(//a[@title='Dresses'][normalize-space()='Dresses'])[2]"
    summer_dresses_xpath = "(//a[@title='Summer Dresses'][normalize-space()='Summer Dresses'])[2]"
    casual_dresses_xpath = "(//a[@title='Casual Dresses'][normalize-space()='Casual Dresses'])[2]"
    sizeL_id = "layered_id_attribute_group_3"
    sizeM_id = "layered_id_attribute_group_2"
    sizeS_id = "layered_id_attribute_group_1"
    slider = "//div[@class='layered_price']//a[1]"
    greenColor = "layered_id_attribute_group_15"
    yellowColor = "layered_id_attribute_group_16"
    blueColor = "layered_id_attribute_group_14"
    img_hov_xpath = "(//img[@title='Printed Summer Dress'])[2]"
    addToCart_onHover_xpath = "(//a[@title='Add to cart'])[1]"
    continue_shopping_xpath = "(//span[@title='Continue shopping'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def dresses_menu_hover(self):
        dresses = self.driver.find_element(By.XPATH, self.dresses_menu_xpath)
        ac = ActionChains(self.driver)
        ac.move_to_element(dresses).perform()
        summer_dresses = self.driver.find_element(By.XPATH, self.summer_dresses_xpath)
        summer_dresses.click()

    def casual_dresses_menu_hover(self):
        dresses = self.driver.find_element(By.XPATH, self.dresses_menu_xpath)
        ac = ActionChains(self.driver)
        ac.move_to_element(dresses).perform()
        summer_dresses = self.driver.find_element(By.XPATH, self.casual_dresses_xpath)
        summer_dresses.click()

    def chooseSize(self, size):
        if size == "l":
            self.driver.find_element(By.ID, self.sizeL_id).click()

        elif size == "m":
            self.driver.find_element(By.ID, self.sizeM_id).click()
        elif size == "s":
            self.driver.find_element(By.ID, self.sizeS_id).click()
        else:
            print("Please pick right size")

    def price_slider(self):
        slid = self.driver.find_element(By.XPATH, self.slider)
        ac = ActionChains(self.driver)
        ac.drag_and_drop_by_offset(slid, 60, 0).perform()

    def chooseColor(self, color):
        if color == "blue":
            self.driver.find_element(By.ID, self.blueColor).click()
        elif color == "green":
            self.driver.find_element(By.ID, self.greenColor).click()
        elif color == "yellow":
            self.driver.find_element(By.ID, self.yellowColor).click()

    def hoverImage(self):
        imgHover = self.driver.find_element(By.XPATH, self.img_hov_xpath)
        ac = ActionChains(self.driver)
        ac.move_to_element(imgHover).perform()




