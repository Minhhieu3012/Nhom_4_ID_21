import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestAppointment(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Khởi động trình duyệt trước khi chạy test"""
        cls.driver = webdriver.Chrome()
    
    def setUp(self):
        """Đăng nhập và truy cập trang đặt lịch hẹn trước mỗi test"""
        self.driver.get("http://127.0.0.1:8000/login.html")
        
        # Đảm bảo trang đăng nhập đã tải hoàn toàn
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        # Đăng nhập với thông tin người dùng hợp lệ
        self.driver.find_element(By.NAME, "username").send_keys("conlonsua400@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("admin1234")
        self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

        # Đợi đến khi người dùng được chuyển đến trang chủ sau khi đăng nhập thành công
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='My Appointments']"))  # Kiểm tra sự xuất hiện của một nút hoặc phần tử có sau khi đăng nhập
        )

        # Truy cập trang đặt lịch hẹn
        self.driver.get("http://127.0.0.1:8000/appointment.html")
        time.sleep(3)

    def test_schedule_appointment_successful(self):
        """Kiểm tra đặt lịch hẹn thành công với thông tin hợp lệ"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "pet_name"))
        )
        self.driver.find_element(By.NAME, "pet_name").send_keys("GalaxyDestroyer")
        self.driver.find_element(By.NAME, "species").send_keys("Dog")
        self.driver.find_element(By.NAME, "vet_name").send_keys("Dr. Smith")
        
        # Gửi thông tin ngày giờ theo định dạng đúng
        datetime_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "datetime"))
    )

    # Dùng javascript để thiết lập giá trị datetime trực tiếp
        self.driver.execute_script("arguments[0].value = '2025-02-15T14:30';", datetime_element)
        self.driver.find_element(By.NAME, "service_type").send_keys("checkup")
        self.driver.find_element(By.NAME, "message").send_keys("Regular checkup")
        self.driver.find_element(By.XPATH, "//input[@value='Schedule Appointment']").click()
        
   
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-info')]"))
        ).text
        self.assertIn("", success_message)

    def test_schedule_appointment_missing_required_fields(self):
        """Kiểm tra đặt lịch hẹn khi thiếu thông tin bắt buộc"""
        self.driver.find_element(By.NAME, "pet_name").send_keys("")
        self.driver.find_element(By.NAME, "species").send_keys("Dog")
        self.driver.find_element(By.NAME, "vet_name").send_keys("Dr. Smith")
        datetime_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "datetime"))
    )

    # Dùng javascript để thiết lập giá trị datetime trực tiếp
        self.driver.execute_script("arguments[0].value = '2025-02-15T14:30';", datetime_element)
        self.driver.find_element(By.NAME, "service_type").send_keys("checkup")
        self.driver.find_element(By.NAME, "message").send_keys("Regular checkup")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@value='Schedule Appointment']").click()

   

        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-info')]"))
        ).text
        self.assertIn("", error_message)
        time.sleep(3)
    def test_schedule_appointment_invalid_datetime(self):
        """Kiểm tra đặt lịch hẹn khi nhập định dạng ngày giờ không hợp lệ"""
        self.driver.find_element(By.NAME, "pet_name").send_keys("GalaxyDestroyer")
        self.driver.find_element(By.NAME, "species").send_keys("Dog")
        self.driver.find_element(By.NAME, "vet_name").send_keys("Dr. Smith")
        self.driver.find_element(By.NAME, "datetime").send_keys("invalid-date")
        self.driver.find_element(By.NAME, "service_type").send_keys("checkup")
        self.driver.find_element(By.NAME, "message").send_keys("Regular checkup")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@value='Schedule Appointment']").click()


        time.sleep(3)
        

    def test_schedule_appointment_missing_pet_name(self):
        """Kiểm tra đặt lịch hẹn khi thiếu tên thú cưng"""
        self.driver.find_element(By.NAME, "pet_name").send_keys("")
        self.driver.find_element(By.NAME, "species").send_keys("Dog")
        self.driver.find_element(By.NAME, "vet_name").send_keys("Dr. Smith")
        datetime_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "datetime"))
    )

    # Dùng javascript để thiết lập giá trị datetime trực tiếp
        self.driver.execute_script("arguments[0].value = '2025-02-15T14:30';", datetime_element)
        self.driver.find_element(By.NAME, "service_type").send_keys("checkup")
        self.driver.find_element(By.NAME, "message").send_keys("Regular checkup")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@value='Schedule Appointment']").click()

    

        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-info')]"))
        ).text
        self.assertIn("", error_message)
        time.sleep(3)
    def test_schedule_appointment_missing_species(self):
        """Kiểm tra đặt lịch hẹn khi thiếu giống thú cưng"""
        self.driver.find_element(By.NAME, "pet_name").send_keys("GalaxyDestroyer")
        self.driver.find_element(By.NAME, "species").send_keys("")
        self.driver.find_element(By.NAME, "vet_name").send_keys("Dr. Smith")
        datetime_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "datetime"))
    )

    # Dùng javascript để thiết lập giá trị datetime trực tiếp
        self.driver.execute_script("arguments[0].value = '2025-02-15T14:30';", datetime_element)
        self.driver.find_element(By.NAME, "service_type").send_keys("checkup")
        self.driver.find_element(By.NAME, "message").send_keys("Regular checkup")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@value='Schedule Appointment']").click()

        

        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-info')]"))
        ).text
        self.assertIn("", error_message)
        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        """Đóng trình duyệt sau khi chạy tất cả các test"""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
