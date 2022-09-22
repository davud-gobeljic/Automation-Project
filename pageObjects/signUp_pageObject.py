import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SignUp():

    signIN_xpath = "//a[normalize-space()='Sign in']"
    inputEmail_id = "email_create"
    submitBTN_id = "SubmitCreate"

    genderMale_id = "id_gender1"
    genderFemale_id = "id_gender2"
    firstName_id = "customer_firstname"
    lastName_id = "customer_lastname"
    password_id = "passwd"
    day_birth_id = "days"
    month_birth_id = "months"
    year_birth_id = "years"
    newsletter_id = "newsletter"
    recive_offers_id = "optin"
    firstNameAddress_id = "firstname"
    lastNameAddress_id = "lastname"
    company_id = "company"
    address1_id = "address1"
    address2_id = "address2"
    city_id = "city"
    selectState_id = "id_state"
    postalCode_id = "postcode"
    selectCountry_id = "id_country"
    additionalInfo_id = "other"
    homePhone_id = "phone"
    mobilePhone_id = "phone_mobile"
    aliasAddress_id = "alias"
    createAccount_id = "submitAccount"



    def __init__(self, driver):
        self.driver = driver


    def signUp(self):
        self.driver.find_element(By.XPATH, self.signIN_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.inputEmail_id).send_keys(email)

    def submitClick(self):
        self.driver.find_element(By.ID, self.submitBTN_id).click()

    def chooseGender(self, gender):
        if gender == "female":
            self.driver.find_element(By.ID, self.genderFemale_id).click()
        elif gender == "male":
            self.driver.find_element(By.ID, self.genderMale_id).click()
        else:
            print("Please choose an option")

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.firstName_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.lastName_id).send_keys(lastname)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def setDateOfBirth(self,day, month, year):
        sel = Select(self.driver.find_element(By.ID, self.day_birth_id))
        sel.select_by_value(day)

        sel = Select(self.driver.find_element(By.ID, self.month_birth_id))
        sel.select_by_value(month)

        sel = Select(self.driver.find_element(By.ID, self.year_birth_id))
        sel.select_by_value(year)

    def newsletter(self):
        self.driver.find_element(By.ID, self.newsletter_id).click()

    def receiveOffers(self):
        self.driver.find_element(By.ID, self.recive_offers_id).click()

    def setAdressFirstName(self, addressfirstName):

        self.driver.find_element(By.ID, self.firstNameAddress_id).send_keys(addressfirstName)

    def setAdressLastName(self, addresslastName):
        self.driver.find_element(By.ID, self.lastNameAddress_id).send_keys(addresslastName)

    def setCompany(self, company):
        self.driver.find_element(By.ID, self.company_id).send_keys(company)

    def setAddress(self, address):
        self.driver.find_element(By.ID, self.address1_id).send_keys(address)

    def setAddress2(self, address2):
        self.driver.find_element(By.ID, self.address2_id).send_keys(address2)

    def setCity(self, city):
        self.driver.find_element(By.ID, self.city_id).send_keys(city)

    def setState(self, state):
        sel = Select(self.driver.find_element(By.ID, self.selectState_id))
        sel.select_by_visible_text(state)

    def postalCode(self, postalcode):
        self.driver.find_element(By.ID, self.postalCode_id).send_keys(postalcode)

    def additionalInfo(self, info):
        self.driver.find_element(By.ID, self.additionalInfo_id).send_keys(info)

    def setPhones(self, home, mobile):
        self.driver.find_element(By.ID, self.homePhone_id).send_keys(home)
        self.driver.find_element(By.ID, self.mobilePhone_id).send_keys(mobile)

    def createAccount(self):
        self.driver.find_element(By.ID, self.createAccount_id).click()


















