import unittest
from tests.home.login_tests import LoginTests
from tests.register.register_multi_tests import RegisterMultiTests


# This test suite loads all test modules, but only collect test cases marked by {marker}
# Py.test -v -s {path}/testsuite.py [-m {marker}] --browser firefox --html=report.html
# Py.test -v -s {path}/testsuite.py [-m {marker}] --browser iexplorer --html=report.html
# Py.test -v -s {path}/testsuite.py [-m {marker}] --browser chrome --html=report.html


# Can create test suite for subset of test modules
# http://stackoverflow.com/questions/15691587/running-a-test-suite-an-arbitrary-collection-of-tests-with-py-test


