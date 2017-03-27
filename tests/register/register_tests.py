from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from pages.courses.register_page import RegisterPage
from pages.courses.courses_page import CoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.cp = CoursesPage(self.driver)
        self.rp = RegisterPage(self.driver)
        #self.ts = TestStatus(self.driver)

    # Test workflow mimics user actions
    def test_register_course(self):
        self.cp.searchCourse("javascript")
        self.cp.clickOnCourse("JavaScript for beginners")
        self.cp.clickOnEnrollButton()
        self.rp.enterCreditCardInformation("12345","1234","123","Canada")
        self.rp.clickVerifyCardButton()


    def test_verifyCreditCard(self):
        result = self.rp.verifyInvalidCreditCard()
        assert result == True

