from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from pages.courses.register_page import RegisterPage
from pages.courses.courses_page import CoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import unittest
import pytest
import time



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultiTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.cp = CoursesPage(self.driver)
        self.rp = RegisterPage(self.driver)
        self.nav = NavigationPage(self.driver)

    #Check if logged in before each test
    def setUp(self):
        if not self.nav.isLoggedIn():
            self.lp.login("test@email.com", "abcabc")

        self.nav.clickOnAllCourses()


    # Test workflow mimics user actions
    @pytest.mark.regression
    @data(*getCSVData("C:\\Python_tests\\Selenium_tests\\Udemy\\FrameworkTest\\testCourses.csv"))
    @unpack
    def test_register_course(self, courseName, ccNum, ccExp, ccCVV, ccCountry):
        self.cp.searchCourse(courseName)
        self.cp.clickOnCourse(courseName)
        self.cp.clickOnEnrollButton()
        self.rp.enterCreditCardInformation(ccNum,ccExp,ccCVV,ccCountry)
        self.rp.clickVerifyCardButton()
        result = self.rp.verifyInvalidCreditCard()
        assert result == True





    # def test_verifyCreditCard(self):
    #     result = self.rp.verifyInvalidCreditCard()
    #     assert result == True

