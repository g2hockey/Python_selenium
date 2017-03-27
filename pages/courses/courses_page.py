import time
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage


class CoursesPage(BasePage):

    def __init__(self, driver):
        super(CoursesPage,self).__init__(driver)
        self.driver = driver

    # Locators
    _usericon = "//*[@id='navbar']//span[text()='User Settings']"
    _searchcourses_field = "search-courses"
    _course_link = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _enroll_button = "enroll-button"
    _all_courses_link = "All Courses"


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





