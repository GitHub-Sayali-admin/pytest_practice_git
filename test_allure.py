# import selenium.common.exceptions
# from allure_commons.types import AttachmentType
# from selenium import webdriver
# import allure
# import pytest
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
#
# @allure.severity(allure.severity_level.NORMAL)
# class TestAllure:
#     @allure.severity(allure.severity_level.MINOR)
#     def test_Logo(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("https://opensource-demo.orangehrmlive.com/")
#         status = self.driver.find_element(By.CSS_SELECTOR, "img[alt='company-branding']")
#         if status==True:
#             assert True
#         else:
#             assert False
#         self.driver.close()
#
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_Listemployees(self):
#         pytest.skip('Skipping test..Later I will implement.')
#
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_Login(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("https://opensource-demo.orangehrmlive.com/")
#         self.driver.find_element(By.NAME, "username").send_keys("Admin")
#         self.driver.find_element(By.NAME, "Password").send_keys("admin123")
#         self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
#         act_title = self.driver.title
#
#         if act_title == "OrangeHRM123":
#             self.driver.close()
#             assert True
#         else:
#             allure.attach(self.driver.get_screenshot_as_png(), name="tesyloginScreen", attachment_type=AttachmentType.PNG)
#             self.driver.close()
#             assert False


# config interpreter
# pip install selenium
# pip install pytest - for test run
# pip install pytest-html - to generate report
# pip install pytest-xdist - to run parallel
# Select pytest as default runner in python (Go to setting --> Tools-->integrated Tools

from selenium import webdriver


# file name should start with test_
# class name should start with Test_
# testcases should start with  test_

# To run the test files from terminal--> pytest
# For more details on lib/ plugins--> pytest -v
# For printing the output on console --> pytest -s
# To run specific file in project dir --> pytest filename.py (eg. pytest test_file_001.py)
# To run testcases parallel --> pytest -n=number (eg. pytest -n=2) number--> worker processor
# To generate html report -->


class Test_Credence_001:

    def test_sum_001(self):
        a = 3
        b = 7
        sum = a + b
        print("Sum of a and b is :" + str(sum))
        if sum == 10:
            assert True
        else:
            assert False

    def test_CredenceUrl_002(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("You are at credence.in")
            driver.close()
            assert True
        else:
            print("You are at Wrong url")
            driver.close()
            assert False


    def test_sub_003(self):
        a = 3
        b = 7
        sub = a - b
        print("Subtraction of a from b is :" + str(sub))
        if sub == -4:
            assert True
        else:
            assert False
