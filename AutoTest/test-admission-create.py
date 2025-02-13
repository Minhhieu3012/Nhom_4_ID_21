
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class TestAdmissionCreate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  
        self.driver.get("http://127.0.0.1:8000/admission-create") 
        self.driver.maximize_window()

# *** CASE 1: NHẬP VIỆN VỚI DỮ LIỆU HỢP LỆ
    def test_valid_admission(self):
        driver = self.driver
        
        # Chờ dropdown pet xuất hiện
        pet = driver.find_element(By.NAME, "pet")
        pet_select = Select(pet)
        pet_select.select_by_index(0)

        room = driver.find_element (By.NAME, "room")
        room_select = Select(room)
        room_select.select_by_index(0)  

        admission_date = driver.find_element(By.NAME, "admission_date")
        admission_date.send_keys("12/02/002025:12:00SA")
        time.sleep(3)

        # Nhấp vào Xác nhận
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(3)

        self.assertIn("admission-list", driver.current_url)
        print("Admission Create Test Passed!")
        time.sleep(5)


# *** CASE2: NGÀY XUẤT VIỆN TRƯỚC NGÀY NHẬP VIỆN
    def test_discharge_before_admission(self):
        driver = self.driver

        pet = driver.find_element(By.NAME, "pet")
        pet_select = Select(pet)  
        pet_select.select_by_index(0) 
       
        room = driver.find_element(By.NAME, "room")
        room_select = Select(room) 
        room_select.select_by_index(0) 

        # Nhập ngày nhập viện (hôm nay) và ngày xuất viện (hôm qua)
        admission_date = driver.find_element(By.NAME, "admission_date")
        admission_date.send_keys("12/02/002025:12:00SA")

        discharge_date = driver.find_element(By.NAME, "discharge_date")
        discharge_date.send_keys("11/02/002025:12:00SA")

        driver.find_element(By.CLASS_NAME, "btn-primary").click()

        time.sleep(3)
        error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Ngày xuất viện không thể trước ngày nhập viện!", error_message)
        print("✅ Test discharge before admission passed!")

# CASE 3: NHẬP NĂM QUÁ 4 CHỮ SỐ
    def test_invalid_admission_year(self):
        driver = self.driver

        pet = driver.find_element (By.NAME, "pet")
        pet_select = Select(pet)
        pet_select.select_by_index(0)

        room = driver.find_element (By.NAME, "room")
        room_select = Select(room)
        room_select.select_by_index(0)

        # Nhập năm sai
        admission_date = driver.find_element(By.NAME, "admission_date")
        admission_date.send_keys("12-02-020000:12:00SA")
        time.sleep(3)

        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(3)

        
        error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Vui lòng nhập đúng định dạng ngày!", error_message)
        print("✅ Test invalid admission year passed!")
    

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
