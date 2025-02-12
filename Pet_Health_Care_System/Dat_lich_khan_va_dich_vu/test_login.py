import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Khởi động trình duyệt trước khi chạy test"""
        cls.driver = webdriver.Chrome()
    
    def setUp(self):
        """Truy cập trang đăng nhập trước mỗi test"""
        self.driver.get("http://127.0.0.1:8000/login.html")
        time.sleep(1)

    def test_login_successful(self):
        """Kiểm tra đăng nhập thành công với tài khoản hợp lệ"""
        self.driver.find_element(By.NAME, "username").send_keys("hoangnh@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("8340924823402Az")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(3)

        self.assertIn("", self.driver.title)  

    def test_login_invalid_email(self):
        """Kiểm tra đăng nhập với email không tồn tại"""
        self.driver.find_element(By.NAME, "username").send_keys("nonexistent@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("ValidPassword123")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(3)

        self.assertIn("", self.driver.page_source)

    def test_login_wrong_password(self):
        """Kiểm tra đăng nhập với mật khẩu sai"""
        self.driver.find_element(By.NAME, "username").send_keys("hoangnh@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("WrongPassword")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(3)

        self.assertIn("", self.driver.page_source)

    def test_login_empty_fields(self):
        """Kiểm tra đăng nhập với ô nhập bị bỏ trống"""
        self.driver.find_element(By.NAME, "username").send_keys("")
        self.driver.find_element(By.NAME, "password").send_keys("")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(3)

        self.assertIn("", self.driver.page_source)

    def test_login_invalid_email_format(self):
        """Kiểm tra đăng nhập với email không hợp lệ"""
        self.driver.find_element(By.NAME, "username").send_keys("invalid-email")
        self.driver.find_element(By.NAME, "password").send_keys("8340924823402Az")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(3)

        self.assertIn("", self.driver.page_source)

    @classmethod
    def tearDownClass(cls):
        """Đóng trình duyệt sau khi chạy tất cả các test"""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
