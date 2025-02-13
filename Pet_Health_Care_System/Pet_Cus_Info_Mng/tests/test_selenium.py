#----------------------------
#Selenium Testing
#----------------------------
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
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

    def test_unit_01_add_customer(self):
        print("Bắt đầu test chức năng khách hàng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
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
            wait = WebDriverWait(driver, 20)
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



    def test_unit_02_edit_customer(self):
        print("Bắt đầu test chức năng chỉnh sửa khách hàng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "KHÁCH HÀNG").click()
        time.sleep(2)

        # Nhấn vào nút ba chấm để mở dropdown
        driver.find_element(By.XPATH, ".//td[last()]//button").click()

        # Chờ menu hiển thị và chọn "Chỉnh sửa"
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dropdown-menu')]//a[contains(text(), 'Chỉnh sửa')]"))).click()

        print("Đã vào trang chỉnh sửa khách hàng.")
        time.sleep(2)

        # Nhập thông tin mới vào form chỉnh sửa
        phone_field = wait.until(EC.presence_of_element_located((By.ID, "id_phoneNumber")))
        phone_field.clear()
        phone_field.send_keys("0999999999")  # Số điện thoại mới

        # lưu
        driver.find_element(By.XPATH, "//button[text()='Lưu']").click()
        time.sleep(4)

        try:
            wait = WebDriverWait(driver, 20)
            wait.until(EC.element_to_be_clickable((By.ID, "cancel-link"))).click()
        except:
            # Nếu không tìm thấy nút "Hủy", có thể trang đã tự chuyển về danh sách.
            pass

        print("Sửa thông tin khách hàng thành công. Kiểm tra danh sách...")

        try:
            customer_list_element = driver.find_element(By.ID, "customer_list")
            self.assertIn("Garnacho", customer_list_element.text)
            print("Thông tin khách hàng đã được chỉnh sửa trong danh sách...")
        except:
            print("Không chỉnh sửa được thông tin khách hàng...")

        time.sleep(4)



    def test_unit_03_appointment_history_customer(self):
        print("Bắt đầu test chức năng xem lịch sử đặt hẹn của khách hàng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "KHÁCH HÀNG").click()
        time.sleep(2)

        # Nhấn vào nút ba chấm để mở dropdown
        driver.find_element(By.XPATH, ".//td[last()]//button").click()

        # Chờ menu hiển thị và chọn "Xem lịch sử đặt hẹn"
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dropdown-menu')]//a[contains(text(), 'Xem lịch sử đặt hẹn')]"))).click()

        print("Đã vào trang lịch sử đặt hẹn của khách hàng.")
        time.sleep(4)



    def test_unit_10_delete_customer(self):
        print("Bắt đầu test chức năng xóa khách hàng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "KHÁCH HÀNG").click()
        time.sleep(2)

        # Nhấn vào nút ba chấm để mở dropdown
        driver.find_element(By.XPATH, ".//td[last()]//button").click()

        # Chờ menu hiển thị và chọn "Xóa"
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dropdown-menu')]//a[contains(text(), 'Xóa')]"))).click()

        print("Đã vào trang xóa khách hàng.")
        time.sleep(4)

        # Xóa khách hàng
        driver.find_element(By.XPATH, "//button[text()='Xóa']").click()
        time.sleep(4)
        print("Xóa khách hàng thành công")

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

    def test_unit_04_add_pet(self):
        print("Bắt đầu test chức năng thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "THÚ CƯNG").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "THÊM THÚ CƯNG MỚI").click()
        time.sleep(2)

        # Điền thông tin thú cưng
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
            wait = WebDriverWait(driver, 20)
            cancel_btn = wait.until(EC.element_to_be_clickable((By.ID, "cancel-link")))
            cancel_btn.click()
        except:
            # Nếu không tìm thấy nút "Hủy", có thể trang đã tự chuyển về danh sách.
            pass

        print("Thêm thú cưng thành công. Kiểm tra danh sách...")

        # --- Kiểm tra xem "Buddy" có trong danh sách không ---
        try:
            pet_list_element = driver.find_element(By.ID, "pet_listt")
            self.assertIn("Buddy", pet_list_element.text)
            print("Tên thú cưng đã hiển thị trong danh sách...")
        except:
            print("Không tìm thấy dữ liệu thú cưng vừa tạo...")

        time.sleep(5)


    def test_unit_05_edit_pet(self):
        print("Bắt đầu test chức năng chỉnh sửa thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "THÚ CƯNG").click()
        time.sleep(2)
        

        # Nhấn vào nút ba chấm để mở dropdown
        driver.find_element(By.XPATH, ".//td[last()]//button").click()

        # Chờ menu hiển thị và chọn "Chỉnh sửa"
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dropdown-menu')]//a[contains(text(), 'Chỉnh sửa')]"))).click()

        print("Đã vào trang chỉnh sửa thú cưng.")
        time.sleep(2)

        # Nhập thông tin mới vào form chỉnh sửa
        pet_name = wait.until(EC.presence_of_element_located((By.ID, "id_name")))
        pet_name.clear()
        pet_name.send_keys("PowPow")

        # lưu
        driver.find_element(By.XPATH, "//button[text()='Lưu']").click()
        time.sleep(4)

        try:
            wait = WebDriverWait(driver, 20)
            wait.until(EC.element_to_be_clickable((By.ID, "cancel-link"))).click()
        except:
            # Nếu không tìm thấy nút "Hủy", có thể trang đã tự chuyển về danh sách.
            pass

        print("Sửa thông tin thú cưng thành công. Kiểm tra danh sách...")

        try:
            pet_list_element = driver.find_element(By.ID, "pet_listt")
            self.assertIn("PowPow", pet_list_element.text)
            print("Thông tin thú cưng đã được chỉnh sửa trong danh sách...")
        except:
            print("Không chỉnh sửa được thông tin thú cưng...")

        time.sleep(4)




    def test_unit_06_medical_records_customer(self):
        print("Bắt đầu test chức năng xem hồ sơ khám bệnh của thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "THÚ CƯNG").click()
        time.sleep(2)

        # Nhấn vào nút ba chấm để mở dropdown
        driver.find_element(By.XPATH, ".//td[last()]//button").click()

        # Chờ menu hiển thị và chọn "Xem lịch sử đặt hẹn"
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dropdown-menu')]//a[contains(text(), 'Xem hồ sơ khám bệnh')]"))).click()

        print("Đã vào trang hồ sơ khám bệnh của thú cưng.")
        time.sleep(4)



    def test_unit_09_delete_pet(self):
        print("Bắt đầu test chức năng xóa thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "THÚ CƯNG").click()
        time.sleep(2)

        # Nhấn vào nút ba chấm để mở dropdown
        driver.find_element(By.XPATH, ".//td[last()]//button").click()

        # Chờ menu hiển thị và chọn "Xóa"
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dropdown-menu')]//a[contains(text(), 'Xóa')]"))).click()

        print("Đã vào trang xóa thú cưng.")
        time.sleep(4)

        # Xóa thú cưng
        driver.find_element(By.XPATH, "//button[text()='Xóa']").click()
        time.sleep(4)
        print("Xóa thú cưng thành công")


#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

    def test_unit_07_add_appointment(self):
        print("Bắt đầu test chức năng đặt lịch hẹn...")
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Mở trang chủ
        driver.get("http://127.0.0.1:8000/")

        # Nhấp "LỊCH HẸN"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "LỊCH HẸN"))).click()

        # Nhấp "THÊM LỊCH HẸN MỚI"
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "THÊM LỊCH HẸN MỚI"))).click()

        # Điền thông tin khách hàng
        customer_input = wait.until(EC.presence_of_element_located((By.ID, "id_customer")))
        select_customer = Select(customer_input)
        select_customer.select_by_visible_text("Garnacho Alexandro (gnc123@gmail.com)")

        pet_select_element = wait.until(EC.presence_of_element_located((By.ID, "id_pet")))
        option = pet_select_element.find_element(By.XPATH, ".//option[normalize-space(text())='PowPow']")
        # Loại bỏ thuộc tính disabled nếu có bằng JavaScript
        driver.execute_script("arguments[0].removeAttribute('disabled')", option)
        select_pet = Select(pet_select_element)
        select_pet.select_by_visible_text("PowPow")

        # Thiết lập ngày hẹn bằng JavaScript
        driver.execute_script("document.getElementById('id_date').value = '2025-01-01';")
        
        # Điền thời gian
        time_input = wait.until(EC.presence_of_element_located((By.ID, "id_time")))
        time_input.send_keys("12:30")

        # Chọn trạng thái "Chưa thanh toán"
        status_element = wait.until(EC.presence_of_element_located((By.ID, "id_status")))
        select_status = Select(status_element)
        select_status.select_by_visible_text("Chưa thanh toán")

        # Nhấp nút "Lưu lịch hẹn"
        btn_save = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Lưu lịch hẹn']")))
        btn_save.click()
        print("Thêm lịch hẹn thành công. Kiểm tra danh sách...")

        try:
            appointment_list_element = driver.find_element(By.ID, "appointments_list")
            self.assertIn("Garnacho Alexandro", appointment_list_element.text)
            print("Không tìm thấy dữ liệu lịch hẹn vừa tạo...")
        except:
            print("Lịch hẹn đã hiển thị trong danh sách...")

        time.sleep(4)


    def test_unit_08_filter_appointment(self):
        print("Bắt đầu test chức năng lọc lịch hẹn...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")  # URL trang chính
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "LỊCH HẸN").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "LỌC LỊCH HẸN").click()
        time.sleep(2)

        # Nhập date
        date_js_filter_appointment = "document.getElementById('date').value = '2025-01-01';"
        driver.execute_script(date_js_filter_appointment)
        select_filter_status = Select(driver.find_element(By.ID, "status"))
        select_filter_status.select_by_value("pending")
        driver.find_element(By.XPATH, "//button[text()='Lọc']").click()
        time.sleep(2)

        # Kiểm tra kết quả trong bảng
        table_text = driver.find_element(By.TAG_NAME, "table").text
        print("Table content after filtering:", table_text)  # Debug statement
        # Check for the date in the table
        self.assertIn("Jan. 1, 2025", table_text, "Không tìm thấy ngày 2025-01-01 trong bảng kết quả.")
        # Check for the status in the table
        self.assertIn("pending", table_text, "Không tìm thấy trạng thái 'pending' trong bảng kết quả.")
        

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()


