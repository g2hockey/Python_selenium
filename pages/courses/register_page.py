import time
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super(RegisterPage,self).__init__(driver)
        self.driver = driver

    # Locators
    _invalidinput = "//*[@id='new_user']//div[contains(text(),'Invalid email or password')]"
    _searchcourses_field = "search-courses"
    _course_link = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _enroll_button = "enroll-button"


    _review_order = "//h1[contains(text(),'Review Your Order')]"
    _cc_num = "cc_field"
    _cc_exp = "cc-exp"
    _cc_cvv = "cc_cvc"
    _cc_country = "country-select-inside"
    _cc_verify = "verify_cc_btn"

    _invalidCreditCard = "//div[@class='payment-errors invalid_number'][contains(text(),'card number is invalid')]"

    #Methods for web element
    def searchCourse(self,courseName):
        searchfield = self.waitForElementVisible(self._searchcourses_field,'id')
        self.sendKeys(courseName, element=searchfield)

    def clickOnCourse(self,fullCourseName):
        self.elementClick(locator=self._course_link.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        enrollbtn = self.waitForElementVisible(self._enroll_button, 'id')
        enrollbtn.location_once_scrolled_into_view
        self.elementClick(element=enrollbtn)

    def enterCardNum(self, num):
        self.sendKeys(num, locator=self._cc_num)

    def enterCardExp(self, exp):
        self.sendKeys(exp, locator=self._cc_exp)

    def enterCardCVV(self, cvv):
        self.sendKeys(cvv, locator=self._cc_cvv)

    def selectCardCountry(self,country):
        self.elementSelect(country,self._cc_country,'id')

    def clickVerifyCardButton(self):
        self.elementClick(locator=self._cc_verify, locatorType='id')


    #Method to perform a workflow
    def enterCreditCardInformation(self, num, exp, cvv, country):
        self.waitForElementVisible(self._review_order, 'xpath')
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.selectCardCountry(country)


    def verifyInvalidCreditCard(self):
        messageElement = self.waitForElementVisible(self._invalidCreditCard, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result


    # def registerCourse(self, courseName):
    #     self.sendKeys(courseName, self._searchcourses_field, 'id')
    #     self.elementClick(self._course_link, 'xpath')
    #
    #     enrollbtn = self.waitForElementVisible(self._enroll_button, 'id')
    #     enrollbtn.location_once_scrolled_into_view
    #     self.elementClick(element=enrollbtn)

    # def enterCreditInfo(self, ccNum, ccExp, ccCVC, ccCountry):
    #     self.waitForElementVisible(self._review_order, 'xpath')
    #     self.sendKeys(ccNum,self._cc_num,'id')
    #     self.sendKeys(ccExp, self._cc_exp, 'id')
    #     self.sendKeys(ccCVC, self._cc_cvv, 'id')
    #     self.elementSelect(ccCountry,self._cc_country,'id')
    #     self.elementClick(self._cc_verify,'id')

