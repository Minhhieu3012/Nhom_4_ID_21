#------------------------------------------------------------------------------------------
# Đây là file thử nghiệm. Toàn bộ test chính thức đã được chuyển sang thư mục AutoTest.
#------------------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import unittest

# class LoginTest(unittest.TestCase):
#     def setUp(self):
#         Setup the WebDriver (Chrome in this example)
#         self.driver = webdriver.Chrome()
#         self.driver.get("https://example.com/login")

#     def test_valid_login(self):
#         driver = self.driver
#         Find elements and perform actions
#         username = driver.find_element(By.ID, "username")
#         password = driver.find_element(By.ID, "password")
#         submit_button = driver.find_element(By.ID, "submit")

#         Input valid credentials and submit
#         username.send_keys("valid_user")
#         password.send_keys("valid_password")
#         submit_button.click()

#         Assert expected outcome (e.g., redirection or welcome message)
#         welcome_message = driver.find_element(By.ID, "welcome")
#         self.assertIn("Welcome", welcome_message.text)

#     def tearDown(self):
#         Close the browser
#         self.driver.quit()

# if _name_ == "__main__":
#     unittest.main()
#-------------------------------------------------------------------------------------------------
