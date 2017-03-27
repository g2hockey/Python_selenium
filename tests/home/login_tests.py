from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest
import pytest, time
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    #setUp only for tests in this class
    def setUp(self):
        if self.nav.isLoggedIn():
            self.lp.logout()


    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    def test_validLogin(self):

        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Login Verification")
        #assert result1 == True

        result2 = self.lp.verifyLoginTitle()
        self.ts.markFinal("test_validLogin", result2, "Title Verification")
        #assert result2 == True
        time.sleep(2)

    @pytest.mark.run(order=2)
    @pytest.mark.regression
    @data(*getCSVData("C:\\Python_tests\\Selenium_tests\\Udemy\\FrameworkTest\\testLogins.csv"))
    @unpack
    def test_invalidLogin(self, email, password):

        self.lp.login(email, password)
        result = self.lp.verifyLoginFailed()
        assert result == True
        #clear text field before next test
        self.lp.clearEmail()


    # def test_verifyTitle(self):
    #     result = self.lp.verifyLoginTitle()
    #     assert result == True

