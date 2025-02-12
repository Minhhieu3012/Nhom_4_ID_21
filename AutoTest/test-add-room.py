import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestRoomAdd(unittest.TestCase):
    def setUp(self):
       # """Khởi động trình duyệt"""
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/room-add/")

    def test_valid_add_room(self):
        #"""Test thêm phòng dữ liệu hợp lệ """
        driver = self.driver

        # Nhập dữ liệu vào form
        room_type = driver.find_element(By.NAME, "room_type")  # Cập nhật nếu ID/NAME khác
        room_type.send_keys("Standard")

        capacity = driver.find_element(By.NAME, "capacity")
        capacity.send_keys("5")

        status = driver.find_element(By.NAME, "status")
        status.send_keys("Available")
        time.sleep(5)
        # Nhấn nút Submit (giả sử có ID là "submit-btn")
        submit_button = driver.find_element(By.CLASS_NAME, "btn-primary") # Thay đổi nếu cần
        submit_button.click()

        # Chờ để trang load sau khi thêm phòng
        time.sleep(3)

        # Kiểm tra URL có chuyển hướng về danh sách phòng không
        self.assertIn("rooms", driver.current_url)

    def test_missing_fields(self):
        """Test bỏ trống một hoặc nhiều trường"""
        driver = self.driver
        driver.find_element(By.NAME, "room_type").send_keys("Luxury")
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(2)

        # Kiểm tra vẫn còn trên trang room-add (không redirect)
        self.assertIn("room-add", driver.current_url)


    def test_negative_capacity(self):
        """Test nhập số âm vào capacity"""
        driver = self.driver
        driver.find_element(By.NAME, "room_type").send_keys("Standard")
        driver.find_element(By.NAME, "capacity").send_keys("-5")  # Nhập số âm
        driver.find_element(By.NAME, "status").send_keys("Available")
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(5)

        self.assertIn("room-add", driver.current_url)

    def test_extreme_capacity(self):
        """Test nhập số quá lớn vào capacity"""
        driver = self.driver
        driver.find_element(By.NAME, "room_type").send_keys("Standard")
        driver.find_element(By.NAME, "capacity").send_keys("99999")  # Nhập số rất lớn
        driver.find_element(By.NAME, "status").send_keys("Available")
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(5)

        self.assertIn("room-add", driver.current_url)

    def tearDown(self):
        """Đóng trình duyệt"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
