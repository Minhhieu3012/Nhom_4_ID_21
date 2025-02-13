import unittest
from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.common.keys import Keys  # type: ignore
import time

class TestRoomAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/room-add/")

# *** CASE 1: THÊM PHÒNG DỮ LIỆU HỢP LỆ
    def test_valid_add_room(self):
        driver = self.driver

        room_type = driver.find_element(By.NAME, "room_type") 
        room_type.send_keys("Standard")

        capacity = driver.find_element(By.NAME, "capacity")
        capacity.send_keys("5")

        status = driver.find_element(By.NAME, "status")
        status.send_keys("Available")
        time.sleep(3)
    
        submit_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        submit_button.click()

        
        time.sleep(3)

        
        self.assertIn("rooms", driver.current_url)

# *** CASE 2: THÊM PHÒNG BỎ TRỐNG TRƯỜNG BẤT KÌ
    def test_missing_fields(self):
        driver = self.driver
        driver.find_element(By.NAME, "room_type").send_keys("Luxury")
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(3)

        # Kiểm tra vẫn còn trên trang room-add (không redirect)
        self.assertIn("room-add", driver.current_url)

# *** CASE 3: NHẬP SỐ ÂM VÀO CAPACITY
    def test_negative_capacity(self):
        driver = self.driver
        driver.find_element(By.NAME, "room_type").send_keys("Standard")
        driver.find_element(By.NAME, "capacity").send_keys("-5")
        driver.find_element(By.NAME, "status").send_keys("Available")
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(3)

        self.assertIn("room-add", driver.current_url)

# *** CASE 4: NHẬP SỐ LỚN VÀO CAPACITY
    def test_extreme_capacity(self):
        driver = self.driver
        driver.find_element(By.NAME, "room_type").send_keys("Standard")
        driver.find_element(By.NAME, "capacity").send_keys("99999")
        driver.find_element(By.NAME, "status").send_keys("Available")
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(3)

        self.assertIn("room-add", driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
