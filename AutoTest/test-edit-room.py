import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class EditRoomTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get("http://localhost:8000/room-edit/1/")
        self.driver.maximize_window()

# *** CASE 1: CHỈNH SỬA PHÒNG DỮ LIỆU HỢP LỆ
    def test_edit_room_valid(self):
        driver = self.driver
        room_type = Select(driver.find_element(By.NAME, "room_type"))
        room_type.select_by_value("Luxury")

        capacity = driver.find_element(By.NAME, "capacity")
        capacity.clear()
        capacity.send_keys("10")

        status = Select(driver.find_element(By.NAME, "status"))
        status.select_by_value("Available")
        time.sleep(3)

        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(3)

        # Kiểm tra kết quả
        self.assertIn("rooms", driver.current_url)

# *** CASE 2: CHỈNH SỬA PHÒNG VỚI SỨC CHỨA NHỎ HƠN 0
    def test_edit_room_negative_capacity(self):
        driver = self.driver

        capacity = driver.find_element(By.NAME, "capacity")
        capacity.clear()
        capacity.send_keys("-5")  # Nhập số âm
        time.sleep(3)
        
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(2)

        error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Sức chứa phải là số dương.", error_message)
        
# *** CASE 3: CHỈNH SỬA PHÒNG VỚI SỨC CHỨA LỚN HƠN 50
    def test_edit_room_overload_capacity(self):
        driver = self.driver

        capacity = driver.find_element(By.NAME, "capacity")
        capacity.clear()
        capacity.send_keys("51")  # Nhập số lớn hơn 50
        time.sleep(3)

        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(2)

        error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Sức chứa không thể vượt quá 50.", error_message)

# *** CASE 4: CHỈNH SỬA PHÒNG KHI ĐỂ TRỐNG TRƯỜNG QUAN TRỌNG
    def test_edit_room_empty_fields(self):
        driver = self.driver
        capacity = driver.find_element(By.NAME, "capacity")
        capacity.clear()  # Xóa dữ liệu
        time.sleep(3)
        
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(3)

        self.assertIn("room-edit", driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
