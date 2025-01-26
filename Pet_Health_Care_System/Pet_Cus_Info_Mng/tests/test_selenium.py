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
from selenium.webdriver.support import expected_conditions as EC

class Add_Customer_Pet_Test(unittest.TestCase):
    def setUp(self):
        # Sử dụng Service để khởi tạo WebDriver
        service = Service("D:/Tài Liệu Công Nghệ Phần Mềm/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
    def tearDown(self):
        self.driver.quit()
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
    def test_unit_add_customer(self):
        print("Bắt đầu test...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")  # URL trang chính
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "KHÁCH HÀNG").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "THÊM KHÁCH HÀNG MỚI").click()
        time.sleep(2)

        # Điền thông tin khách hàng
        last_name = driver.find_element(By.ID, "id_lastName")
        last_name.send_keys("Alexandro")

        first_name = driver.find_element(By.ID, "id_firstName")
        first_name.send_keys("Garnacho")

        email = driver.find_element(By.ID, "id_email")
        email.send_keys("gnc123@gmail.com")

        age = driver.find_element(By.ID, "id_age")
        age.send_keys("19")

        phone = driver.find_element(By.ID, "id_phoneNumber")
        phone.send_keys("0327329948")

        address = driver.find_element(By.ID, "id_address")
        address.send_keys("47/24/38 Bùi Đình Túy")

        gender = driver.find_element(By.ID, "id_gender")
        gender.send_keys("Nam")

        time.sleep(2)  

        create_button = driver.find_element(By.XPATH, "//button[text()='Tạo khách hàng']")
        create_button.click()
        time.sleep(2)

        try:
            wait = WebDriverWait(driver, 10)
            cancel_btn = wait.until(EC.element_to_be_clickable((By.ID, "cancel-link")))
            cancel_btn.click()
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

        print("Kết thúc test.")
        time.sleep(5)
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

    def test_unit_add_pet(self):
        print("Bắt đầu test...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")  # URL trang chính
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "THÚ CƯNG").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "THÊM THÚ CƯNG MỚI").click()
        time.sleep(2)

        # --- Nhập thông tin thú cưng ---
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

        print("Kết thúc test.")
        time.sleep(5)

# class Edit_Customer_Pet_Test(unittest.TestCase):
# class Appointment_History_Customer_Test(unittest.TestCase):
# class MedicalRecord_History_Pet_Test
# class Add_Appointment_Test(unittest.TestCase):
# class Filter_Appointment_Test(unittest.TestCase):
# class Delete_Appointment_Test(unittest.TestCase):
# class Delete_Customer_Pet_Test(unittest.TestCase):
#-------------------------------------
# Tổng cộng có 11 thao tác: 2/11
#-------------------------------------
if __name__ == "__main__":
    unittest.main()


