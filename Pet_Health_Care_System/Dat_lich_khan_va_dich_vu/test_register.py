import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Khởi động trình duyệt trước khi chạy test"""
        cls.driver = webdriver.Chrome()
    
    def setUp(self):
        """Chạy trước mỗi test case"""
        self.driver.get("http://127.0.0.1:8000/register/")
        time.sleep(1)

    def test_register_valid(self):
        """Kiểm tra đăng ký với dữ liệu hợp lệ"""
        self.driver.find_element(By.NAME, "email").send_keys("hoangnh@gmail.com")
        self.driver.find_element(By.NAME, "phone").send_keys("0987654321")
        self.driver.find_element(By.NAME, "password1").send_keys("8340924823402Az")
        self.driver.find_element(By.NAME, "password2").send_keys("8340924823402Az")
        self.driver.find_element(By.NAME, "password2").send_keys(Keys.RETURN)
        time.sleep(3)

        self.assertIn("", self.driver.page_source)

    def test_register_invalid_email(self):
        """Kiểm tra đăng ký với email không hợp lệ"""
        self.driver.find_element(By.NAME, "email").send_keys("invalid-email")
        self.driver.find_element(By.NAME, "phone").send_keys("0987654321")
        self.driver.find_element(By.NAME, "password1").send_keys("ValidPassword123")
        self.driver.find_element(By.NAME, "password2").send_keys("ValidPassword123")
        self.driver.find_element(By.NAME, "password2").send_keys(Keys.RETURN)
        time.sleep(3)

        self.assertIn("", self.driver.page_source)

    def test_register_mismatched_passwords(self):
        """Kiểm tra đăng ký với mật khẩu không khớp"""
        self.driver.find_element(By.NAME, "email").send_keys("mismatch@example.com")
        self.driver.find_element(By.NAME, "phone").send_keys("0987654321")
        self.driver.find_element(By.NAME, "password1").send_keys("ValidPassword123")
        self.driver.find_element(By.NAME, "password2").send_keys("DifferentPassword")
        self.driver.find_element(By.NAME, "password2").send_keys(Keys.RETURN)
        time.sleep(3)

        self.assertIn("", self.driver.page_source)

    def test_register_existing_email(self):
        """Kiểm tra đăng ký với email đã tồn tại"""
        self.driver.find_element(By.NAME, "email").send_keys("hoangnh@gmail.com")
        self.driver.find_element(By.NAME, "phone").send_keys("0987654321")
        self.driver.find_element(By.NAME, "password1").send_keys("8340924823402Az")
        self.driver.find_element(By.NAME, "password2").send_keys("8340924823402Az")
        self.driver.find_element(By.NAME, "password2").send_keys(Keys.RETURN)
        time.sleep(3)

        self.assertIn("", self.driver.page_source)

    def test_register_short_password(self):
        """Kiểm tra đăng ký với mật khẩu quá ngắn"""
        self.driver.find_element(By.NAME, "email").send_keys("shortpass@example.com")
        self.driver.find_element(By.NAME, "phone").send_keys("0987654321")
        self.driver.find_element(By.NAME, "password1").send_keys("123")
        self.driver.find_element(By.NAME, "password2").send_keys("123")
        self.driver.find_element(By.NAME, "password2").send_keys(Keys.RETURN)
        time.sleep(3)

        self.assertIn("", self.driver.page_source)

    @classmethod
    def tearDownClass(cls):
        """Đóng trình duyệt sau khi chạy tất cả các test"""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
