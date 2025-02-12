
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestAdmissionCreate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Khởi tạo trình duyệt Chrome
        self.driver.get("http://127.0.0.1:8000/admission-create")  # Mở trang nhập viện
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)  # Thêm thuộc tính self.wait

    # Nhập viện với dữ liệu hợp lệ
    def test_valid_admission(self):
        driver = self.driver
        
        try:
            # Chờ dropdown pet xuất hiện
            pet_dropdown = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "pet"))
            )
            pet_select = Select(pet_dropdown)
            pet_select.select_by_index(1)  # Chọn thú cưng đầu tiên (có thể thay đổi)

            # Chờ dropdown room xuất hiện
            room_dropdown = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "room"))
            )
            room_select = Select(room_dropdown)
            room_select.select_by_index(1)  # Chọn phòng đầu tiên (có thể thay đổi)

            admission_date = driver.find_element(By.NAME, "admission_date")
            admission_date.send_keys("12/02/002025:12:00SA")

            discharge_date = driver.find_element(By.NAME, "discharge_date")
            discharge_date.send_keys("14/02/002025:13:00CH")
            time.sleep(3)

            # Chờ nút Submit và nhấn vào
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )
            submit_button.click()

            # Kiểm tra xem có chuyển hướng đến danh sách nhập viện không
            WebDriverWait(driver, 10).until(
                EC.url_contains("/admission-list")
            )
            self.assertIn("admission-list", driver.current_url)
            print("✅ Admission Create Test Passed!")
            time.sleep(5)

        except Exception as e:
            print(f"❌ Test Failed: {e}")
            self.fail("Test case failed")
            time.sleep(5)
        
    def test_discharge_before_admission(self):
        driver = self.driver

        pet_select = Select(self.wait.until(EC.presence_of_element_located((By.NAME, "pet"))))
        pet_select.select_by_index(1)

        room_select = Select(self.wait.until(EC.presence_of_element_located((By.NAME, "room"))))
        room_select.select_by_index(1)

        # Nhập ngày nhập viện (hôm nay) và ngày xuất viện (hôm qua)
        admission_date = driver.find_element(By.NAME, "admission_date")
        admission_date.send_keys("12/02/002025:12:00SA")

        discharge_date = driver.find_element(By.NAME, "discharge_date")
        discharge_date.send_keys("11/02/002025:12:00SA")
        time.sleep(3)

        submit_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()

        time.sleep(3)
        # Kiểm tra lỗi hiển thị
        error_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Ngày xuất viện không thể trước ngày nhập viện!')]")))
        self.assertIn("Ngày xuất viện không thể trước ngày nhập viện!", error_message.text)
        print("✅ Test discharge before admission passed!")

    # Test nhập viện với năm quá 4 số
    def test_invalid_admission_year(self):
        driver = self.driver

        pet_select = Select(self.wait.until(EC.presence_of_element_located((By.NAME, "pet"))))
        pet_select.select_by_index(1)

        room_select = Select(self.wait.until(EC.presence_of_element_located((By.NAME, "room"))))
        room_select.select_by_index(1)

        # Nhập năm sai (1000000)
        admission_date = driver.find_element(By.NAME, "admission_date")
        admission_date.send_keys("12-02-200000:12:00SA")
        time.sleep(3)

        submit_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()

        time.sleep(3)
        # Kiểm tra lỗi hiển thị
        error_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Vui lòng nhập đúng định dạng ngày!')]")))
        self.assertIn("Vui lòng nhập đúng định dạng ngày!", error_message.text)
        print("✅ Test invalid admission year passed!")
    

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
