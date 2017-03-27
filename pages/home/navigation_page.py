import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super(NavigationPage,self).__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "My Courses"
    _practice = "Practice"
    _usericon = "//*[@id='navbar']//span[text()='User Settings']"
    _all_courses_link = "All Courses"
    _logout = "Log out"


    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="partial_link")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="partial_link")

    def navigateToUserSettings(self):
        self.elementClick(locator=self._usericon, locatorType="xpath")

    def clickLogout(self):
        self.elementClick(self._logout, locatorType="partial_link")

    def clickOnAllCourses(self):
        allCourseBtn = self.getElement(self._all_courses_link,'partial_link')
        allCourseBtn.location_once_scrolled_into_view
        self.elementClick(element=allCourseBtn)

    def isLoggedIn(self):
        return self.isElementPresent(self._usericon,locatorType="xpath")