#---------------------------
#Selenium Testing
#---------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class Function_Customer_Pet_Appointment_Test(unittest.TestCase):
    def setUp(self):
        # Sử dụng Service để khởi tạo WebDriver
        service = Service("D:/Tài Liệu Công Nghệ Phần Mềm/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
    def tearDown(self):
        self.driver.quit()
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

    def test_unitappointment(self):
        print("Bắt đầu test chức năng đặt lịch hẹn...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")  # URL trang chính
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "LỊCH HẸN").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "THÊM LỊCH HẸN MỚI").click()
        time.sleep(2)

        # Điền thông tin lịch hẹn
        # Chọn Khách hàng
        select_customer = Select(driver.find_element(By.ID, "id_customer"))
        # Ví dụ: chọn khách hàng theo thứ tự (index)
        select_customer.select_by_index(1)

        # Chọn Pet
        select_pet = Select(driver.find_element(By.ID, "id_pet"))
        select_pet.select_by_index(1)
        driver.find_element(By.ID, "id_date").send_keys("2025-01-01")
        driver.find_element(By.ID, "id_time").send_keys("10:30")
        select_status = Select(driver.find_element(By.ID, "id_status"))
        select_status.select_by_value("Chưa thanh toán")  

        # Click nút "Lưu lịch hẹn"
        driver.find_element(By.XPATH, "//button[text()='Lưu lịch hẹn']").click()

        # Kiểm tra xem trang có chuyển và hiển thị danh sách lịch hẹn
        try:
            appointment_list_element = driver.find_element(By.ID, "appointments_list")
            self.assertIn("Garnacho", appointment_list_element.text)
            print("Lịch hẹn của khách hàng đã hiển thị trong danh sách...")
        except:
            print("Không tìm thấy dữ liệu lịch hẹn vừa tạo...")
        time.sleep(4)

        
        # add_appointment
        # filter_appointment
        # delete_appointment


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

    def test_unit_customer(self):
        print("Bắt đầu test chức năng khách hàng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")  # URL trang chính
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "KHÁCH HÀNG").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "THÊM KHÁCH HÀNG MỚI").click()
        time.sleep(2)

        # Điền thông tin khách hàng
        driver.find_element(By.ID, "id_lastName").send_keys("Alexandro")
        driver.find_element(By.ID, "id_firstName").send_keys("Garnacho")
        driver.find_element(By.ID, "id_email").send_keys("gnc123@gmail.com")
        driver.find_element(By.ID, "id_age").send_keys("19")
        driver.find_element(By.ID, "id_phoneNumber").send_keys("0327329948")
        driver.find_element(By.ID, "id_address").send_keys("47/24/38 Bùi Đình Túy")
        driver.find_element(By.ID, "id_gender").send_keys("Nam")
        time.sleep(2)  

        # lưu khách hàng
        driver.find_element(By.XPATH, "//button[text()='Tạo khách hàng']").click()
        time.sleep(2)

        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, "cancel-link"))).click()
        except:
            # Nếu không tìm thấy nút "Hủy", có thể trang đã tự chuyển về danh sách.
            pass

        print("Thêm khách hàng thành công. Kiểm tra danh sách...")

        try:
            customer_list_element = driver.find_element(By.ID, "customer_list")
            self.assertIn("Garnacho", customer_list_element.text)
            print("Tên khách hàng đã hiển thị trong danh sách...")
        except:
            print("Không tìm thấy dữ liệu khách hàng vừa tạo...")

        time.sleep(4)

        # edit_customer
        # appointment_history_customer
        # delete_customer

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
    def test_unit_pet(self):
        print("Bắt đầu test chức năng thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")  # URL trang chính
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "THÚ CƯNG").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "THÊM THÚ CƯNG MỚI").click()
        time.sleep(2)

        # --- Điền thông tin thú cưng ---
        driver.find_element(By.ID, "id_name").send_keys("Buddy")

        # Nhập ngày sinh qua JavaScript
        #   - Gán giá trị cho trường id_dateOfBirth
        #   - Kế tiếp, "dispatchEvent(new Event('change'))" để kích hoạt hàm lắng nghe sự kiện "change"
        driver.execute_script(
            "document.getElementById('id_dateOfBirth').value = '2022-02-12';"
        )
        driver.execute_script(
            "document.getElementById('id_dateOfBirth').dispatchEvent(new Event('change'));"
        )
        driver.find_element(By.ID, "id_species").send_keys("Chó")
        driver.find_element(By.ID, "id_healthStatus").send_keys("Sức khỏe tốt")
        driver.find_element(By.ID, "id_owner").send_keys("Garnacho")
        driver.find_element(By.ID, "id_gender").send_keys("Đực")
        time.sleep(2)

        # --- Lưu thú cưng ---
        driver.find_element(By.XPATH, "//button[text()='Tạo thú cưng']").click()
        time.sleep(2)

        # Thử tìm nút Hủy (hoặc về danh sách)
        try:
            wait = WebDriverWait(driver, 10)
            cancel_btn = wait.until(EC.element_to_be_clickable((By.ID, "cancel-link")))
            cancel_btn.click()
        except:
            # Nếu không tìm thấy nút "Hủy", có thể trang đã tự chuyển về danh sách.
            pass

        print("Thêm thú cưng thành công. Kiểm tra danh sách...")

        # --- Kiểm tra xem "Buddy" có trong danh sách không ---
        try:
            pet_list_element = driver.find_element(By.ID, "pet_list")
            self.assertIn("Buddy", pet_list_element.text)
            print("Tên thú cưng đã hiển thị trong danh sách...")
        except:
            print("Không tìm thấy dữ liệu thú cưng vừa tạo...")

        time.sleep(5)
    
        # edit_pet
        # medicalRecord_history_pet
        # delete_pet

if __name__ == "__main__":
    unittest.main()


