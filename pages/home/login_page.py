import time
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage,self).__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)



    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _usericon = "//*[@id='navbar']//span[text()='User Settings']"
    _invalidinput = "//*[@id='new_user']//div[contains(text(),'Invalid email or password')]"


    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType='id')

    def clearEmail(self):
        self.clearText(self._email_field, locatorType='id')

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType='id')

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    #Method to perform a workflow
    def login(self, email="", password=""):
        self.waitForElementVisible(self._login_link,"partial_link")
        self.clickLoginLink()

        self.waitForElementVisible(self._email_field)
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()


    def logout(self):
        self.waitForElementVisible(self._usericon, 'xpath')
        self.nav.navigateToUserSettings()
        self.nav.clickLogout()

    #Method to verify and return boolean result
    def verifyLoginSuccessful(self):
        result = self.nav.isLoggedIn()
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._invalidinput,'xpath')
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")




