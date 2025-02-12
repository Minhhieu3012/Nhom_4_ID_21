# #---------------------------
# #Selenium Testing
# #---------------------------
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Function_Pet_MedicalRecord_TreatmentProgress_Medication_Notification_Test(unittest.TestCase):
    def setUp(self):
        # Sử dụng Service để khởi tạo WebDriver
        service = Service("D:/Tài Liệu Công Nghệ Phần Mềm/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
    def tearDown(self):
        self.driver.quit()
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

    # def test_unit_pet_create(self):
    #     print("Bắt đầu test chức năng thú cưng...")
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:8000/")
    #     time.sleep(3)

    #     driver.find_element(By.LINK_TEXT, "THÚ CƯNG").click()
    #     time.sleep(2)

    #     driver.find_element(By.LINK_TEXT, "THÊM THÚ CƯNG MỚI").click()
    #     time.sleep(2)

    #     # Điền thông tin thú cưng
    #     driver.find_element(By.ID, "id_name").send_keys("Pepsi")
    #     driver.find_element(By.ID, "id_age").send_keys("10")
    #     driver.find_element(By.ID, "id_species").send_keys("Chó")
    #     # Sửa id này từ "id_healthStatus" thành "id_current_health_status"
    #     driver.find_element(By.ID, "id_current_health_status").send_keys("Sức khỏe tốt")
    #     time.sleep(2)

    #     # --- Lưu thú cưng ---
    #     driver.find_element(By.XPATH, "//button[text()='Tạo thú cưng']").click()
    #     time.sleep(2)

    #     # Thử tìm nút Hủy (hoặc chuyển về danh sách)
    #     try:
    #         wait = WebDriverWait(driver, 20)
    #         cancel_btn = wait.until(EC.element_to_be_clickable((By.ID, "cancel-link")))
    #         cancel_btn.click()
    #     except Exception as e:
    #         print("Không tìm thấy nút Hủy:", e)
    #         # Nếu không tìm thấy nút "Hủy", có thể trang đã tự chuyển hướng.
    #         pass

    #     print("Thêm thú cưng thành công. Kiểm tra danh sách...")
    #     try:
    #         pet_list_element = driver.find_element(By.ID, "pet_list")
    #         self.assertIn("Pepsi", pet_list_element.text)
    #         print("Tên thú cưng đã hiển thị trong danh sách...")
    #     except Exception as e:
    #         print("Không tìm thấy dữ liệu thú cưng vừa tạo:", e)

    #     time.sleep(5)


    # def test_unit_pet_update(self):
    #     print("Bắt đầu test chức năng chỉnh sửa thú cưng...")
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:8000/")
    #     time.sleep(3)

    #     # Vào trang danh sách thú cưng
    #     driver.find_element(By.LINK_TEXT, "THÚ CƯNG").click()
    #     time.sleep(2)
        
    #     # Nhấn vào nút ba chấm của dòng cuối cùng để mở dropdown
    #     driver.find_element(By.XPATH, ".//td[last()]//button").click()
    #     time.sleep(1)
        
    #     # Tìm và click vào liên kết "Xem chi tiết" trong dropdown
    #     wait = WebDriverWait(driver, 20)
    #     xem_chi_tiet_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Xem chi tiết")))
    #     xem_chi_tiet_link.click()
    #     time.sleep(2)
        
    #     print("Đã vào trang chi tiết thú cưng.")
    #     time.sleep(2)
        
    #     # Nhấn nút "CHỈNH SỬA" trên trang chi tiết
    #     driver.find_element(By.LINK_TEXT, "CHỈNH SỬA").click()
    #     time.sleep(2)
        
    #     pet_name = wait.until(EC.presence_of_element_located((By.ID, "id_name")))
    #     pet_name.clear()
    #     pet_name.send_keys("Jack")
        
    #     # Nhấn nút "Lưu" để lưu thay đổi
    #     driver.find_element(By.XPATH, "//button[text()='Lưu']").click()
    #     time.sleep(2)
        
    #     # Sau khi lưu, ứng dụng chuyển hướng về trang danh sách thú cưng.
    #     print("Sau khi lưu, đợi trang danh sách load...")
    #     wait.until(EC.presence_of_element_located((By.ID, "pet_list")))
    #     time.sleep(2)
    

    # def test_unit_pet_delete(self):
    #     print("Bắt đầu test chức năng chỉnh sửa thú cưng...")
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:8000/")
    #     time.sleep(3)

    #     # Vào trang danh sách thú cưng
    #     driver.find_element(By.LINK_TEXT, "THÚ CƯNG").click()
    #     time.sleep(2)
        
    #     # Nhấn vào nút ba chấm của dòng cuối cùng để mở dropdown
    #     driver.find_element(By.XPATH, ".//td[last()]//button").click()
    #     time.sleep(1)
        
    #     # Tìm và click vào liên kết "Xem chi tiết" trong dropdown
    #     wait = WebDriverWait(driver, 20)
    #     xem_chi_tiet_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Xem chi tiết")))
    #     xem_chi_tiet_link.click()
    #     time.sleep(2)
        
    #     print("Đã vào trang chi tiết thú cưng.")
    #     time.sleep(2)
        
    #     driver.find_element(By.LINK_TEXT, "XÓA").click()
    #     time.sleep(2)

    #     print("Đã vào trang xóa thú cưng.")
    #     time.sleep(4)

    #     # Xóa thú cưng
    #     driver.find_element(By.XPATH, "//button[text()='Xóa']").click()
    #     time.sleep(4)
    #     print("Xóa thú cưng thành công")

    
    # def test_unit_pet_medical_record_form(self):
    #     print("Bắt đầu test chức năng xem hồ sơ khám bệnh của thú cưng...")
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:8000/") 
    #     time.sleep(3)

    #     driver.find_element(By.LINK_TEXT, "THÚ CƯNG").click()
    #     time.sleep(2)

    #     # Nhấn vào nút ba chấm của dòng cuối cùng để mở dropdown
    #     driver.find_element(By.XPATH, ".//td[last()]//button").click()
    #     time.sleep(1)
        
    #     # Tìm và click vào liên kết "Xem chi tiết" trong dropdown
    #     wait = WebDriverWait(driver, 20)
    #     xem_chi_tiet_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Xem chi tiết")))
    #     xem_chi_tiet_link.click()
    #     time.sleep(2)
        
    #     print("Đã vào trang chi tiết thú cưng.")
    #     time.sleep(2)
        
    #     # Chuyển sang trang hồ sơ khám bệnh
    #     driver.find_element(By.LINK_TEXT, "XEM HỒ SƠ KHÁM BỆNH").click()
    #     time.sleep(2)

    #     print("Đã vào trang hồ sơ khám bệnh của thú cưng.")
    #     time.sleep(2)

    #     # Nhấn nút thêm bệnh án mới
    #     driver.find_element(By.LINK_TEXT, "THÊM BỆNH ÁN MỚI").click()
    #     time.sleep(2)

    #     print("Đã vào trang tạo bệnh án.")
    #     time.sleep(2)

    #     # Điền thông tin vào form
    #     select_pet = wait.until(EC.element_to_be_clickable((By.NAME, "pet")))
    #     select_pet.click()
    #     select_pet.send_keys(Keys.ARROW_DOWN)  # Chọn thú cưng đầu tiên (có thể cần điều chỉnh)
    #     select_pet.send_keys(Keys.RETURN)
    #     time.sleep(2)

    #     # Nhập ngày khám
    #     date_input = driver.find_element(By.NAME, "date")
    #     date_input.send_keys("12/02/2025")
    #     time.sleep(2)

    #     # Nhập triệu chứng
    #     symptom_input = driver.find_element(By.NAME, "symptoms")
    #     symptom_input.clear()
    #     symptom_input.send_keys("Ho, sốt, biếng ăn")
    #     time.sleep(2)

    #     # Nhập bệnh/chẩn đoán
    #     disease_input = driver.find_element(By.NAME, "disease")
    #     disease_input.send_keys("Cảm cúm do thay đổi thời tiết")
    #     time.sleep(2)

    #     # Nhập ghi chú của bác sĩ
    #     vet_notes_input = driver.find_element(By.NAME, "vet_notes")
    #     vet_notes_input.clear()
    #     vet_notes_input.send_keys("Cần theo dõi thêm, bổ sung vitamin")
    #     time.sleep(2)

    #     wait = WebDriverWait(driver, 20)

    #     # Chờ xem nút có phải "Lưu bệnh án" hoặc "Cập nhật" không
    #     save_button = wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, "//button[contains(text(), 'Lưu') or contains(text(), 'Cập nhật')]")
    #     ))
    #     save_button.click()

    #     print("Bệnh án đã được tạo thành công.")

    #     # Kiểm tra xem bệnh án có xuất hiện trong danh sách không
    #     time.sleep(2)
    #     page_source = driver.page_source
    #     self.assertIn("Ho, sốt, biếng ăn", page_source)
    #     print("Bệnh án đã được lưu và hiển thị trên danh sách.")

    #     time.sleep(4)

    # def test_unit_pet_medical_record_form_edit(self):
    #     print("Bắt đầu test chức năng xem hồ sơ khám bệnh của thú cưng...")
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:8000/") 
    #     time.sleep(3)

    #     driver.find_element(By.LINK_TEXT, "THÚ CƯNG").click()
    #     time.sleep(2)

    #     # Nhấn vào nút ba chấm của dòng cuối cùng để mở dropdown
    #     driver.find_element(By.XPATH, ".//td[last()]//button").click()
    #     time.sleep(1)
        
    #     # Tìm và click vào liên kết "Xem chi tiết" trong dropdown
    #     wait = WebDriverWait(driver, 20)
    #     xem_chi_tiet_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Xem chi tiết")))
    #     xem_chi_tiet_link.click()
    #     time.sleep(2)
        
    #     print("Đã vào trang chi tiết thú cưng.")
    #     time.sleep(2)
        
    #     # Chuyển sang trang hồ sơ khám bệnh
    #     driver.find_element(By.LINK_TEXT, "XEM HỒ SƠ KHÁM BỆNH").click()
    #     time.sleep(2)

    #     print("Đã vào trang hồ sơ khám bệnh của thú cưng.")
    #     time.sleep(2)

    #     driver.find_element(By.LINK_TEXT, "SỬA").click()
    #     time.sleep(2)

    #     print("Đang chỉnh sửa thông tin hồ sơ khám bệnh...")

    #     # Nhập ngày khám
    #     date_input = driver.find_element(By.NAME, "date")
    #     date_input.send_keys("12/02/2025")
    #     time.sleep(2)

    #     # Cập nhập ghi chú của bác sĩ
    #     vet_notes_input = driver.find_element(By.NAME, "vet_notes")
    #     vet_notes_input.clear()
    #     vet_notes_input.send_keys("Cần theo dõi thêm, bổ sung vitamin, bổ sung thêm: cần uống nhiều nước và tái khám thường xuyên")
    #     time.sleep(2)

    #     wait = WebDriverWait(driver, 20)

    #     # Chờ xem nút có phải "Lưu bệnh án" hoặc "Cập nhật" không
    #     save_button = wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, "//button[contains(text(), 'Lưu') or contains(text(), 'Cập nhật')]")
    #     ))
    #     save_button.click()

    #     print("Bệnh án đã được chỉnh sửa thành công.")

    #     # Kiểm tra xem bệnh án có xuất hiện trong danh sách không
    #     time.sleep(2)
    #     page_source = driver.page_source
    #     self.assertIn("Ho, sốt, biếng ăn", page_source)
    #     print("Bệnh án đã được lưu và hiển thị trên danh sách.")

    #     time.sleep(4)


    # def test_unit_pet_medical_record_form_edit(self):
    #     print("Bắt đầu test chức năng xem hồ sơ khám bệnh của thú cưng...")
    #     driver = self.driver
    #     driver.get("http://127.0.0.1:8000/") 
    #     time.sleep(3)

    #     driver.find_element(By.LINK_TEXT, "THÚ CƯNG").click()
    #     time.sleep(2)

    #     # Nhấn vào nút ba chấm của dòng cuối cùng để mở dropdown
    #     driver.find_element(By.XPATH, ".//td[last()]//button").click()
    #     time.sleep(1)
        
    #     # Tìm và click vào liên kết "Xem chi tiết" trong dropdown
    #     wait = WebDriverWait(driver, 20)
    #     xem_chi_tiet_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Xem chi tiết")))
    #     xem_chi_tiet_link.click()
    #     time.sleep(2)
        
    #     print("Đã vào trang chi tiết thú cưng.")
    #     time.sleep(2)
        
    #     # Chuyển sang trang hồ sơ khám bệnh
    #     driver.find_element(By.LINK_TEXT, "XEM HỒ SƠ KHÁM BỆNH").click()
    #     time.sleep(2)

    #     print("Đã vào trang hồ sơ khám bệnh của thú cưng.")
    #     time.sleep(2)

    #     driver.find_element(By.LINK_TEXT, "XÓA").click()
    #     time.sleep(2)

    #     print("Đã vào trang xóa thú cưng.")
    #     time.sleep(4)

    #     # Xóa hồ sơ khám bệnh
    #     driver.find_element(By.XPATH, "//button[text()='Xóa']").click()
    #     time.sleep(4)
    #     print("Xóa hồ sơ khám bệnh thành công")

        









# #------------------------------------------------------------------------------------------------------------
# #------------------------------------------------------------------------------------------------------------

#     def test_unit_07_add_appointment(self):
#         print("Bắt đầu test chức năng đặt lịch hẹn...")
#         driver = self.driver
#         wait = WebDriverWait(driver, 10)

#         # Mở trang chủ
#         driver.get("http://127.0.0.1:8000/")

#         # Nhấp "LỊCH HẸN"
#         wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "LỊCH HẸN"))).click()

#         # Nhấp "THÊM LỊCH HẸN MỚI"
#         wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "THÊM LỊCH HẸN MỚI"))).click()

#         # Điền thông tin khách hàng
#         customer_input = wait.until(EC.presence_of_element_located((By.ID, "id_customer")))
#         select_customer = Select(customer_input)
#         select_customer.select_by_visible_text("Garnacho Alexandro (gnc123@gmail.com)")

#         pet_select_element = wait.until(EC.presence_of_element_located((By.ID, "id_pet")))
#         option = pet_select_element.find_element(By.XPATH, ".//option[normalize-space(text())='PowPow']")
#         # Loại bỏ thuộc tính disabled nếu có bằng JavaScript
#         driver.execute_script("arguments[0].removeAttribute('disabled')", option)
#         select_pet = Select(pet_select_element)
#         select_pet.select_by_visible_text("PowPow")

#         # Thiết lập ngày hẹn bằng JavaScript
#         driver.execute_script("document.getElementById('id_date').value = '2025-01-01';")
        
#         # Điền thời gian
#         time_input = wait.until(EC.presence_of_element_located((By.ID, "id_time")))
#         time_input.send_keys("12:30")

#         # Chọn trạng thái "Chưa thanh toán"
#         status_element = wait.until(EC.presence_of_element_located((By.ID, "id_status")))
#         select_status = Select(status_element)
#         select_status.select_by_visible_text("Chưa thanh toán")

#         # Nhấp nút "Lưu lịch hẹn"
#         btn_save = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Lưu lịch hẹn']")))
#         btn_save.click()
#         print("Thêm lịch hẹn thành công. Kiểm tra danh sách...")

#         try:
#             appointment_list_element = driver.find_element(By.ID, "appointments_list")
#             self.assertIn("Garnacho Alexandro", appointment_list_element.text)
#             print("Không tìm thấy dữ liệu lịch hẹn vừa tạo...")
#         except:
#             print("Lịch hẹn đã hiển thị trong danh sách...")

#         time.sleep(4)


#     def test_unit_08_filter_appointment(self):
#         print("Bắt đầu test chức năng lọc lịch hẹn...")
#         driver = self.driver
#         driver.get("http://127.0.0.1:8000/")  # URL trang chính
#         time.sleep(3)

#         driver.find_element(By.LINK_TEXT, "LỊCH HẸN").click()
#         time.sleep(2)

#         driver.find_element(By.LINK_TEXT, "LỌC LỊCH HẸN").click()
#         time.sleep(2)

#         # Nhập date
#         date_js_filter_appointment = "document.getElementById('date').value = '2025-01-01';"
#         driver.execute_script(date_js_filter_appointment)
#         select_filter_status = Select(driver.find_element(By.ID, "status"))
#         select_filter_status.select_by_value("pending")
#         driver.find_element(By.XPATH, "//button[text()='Lọc']").click()
#         time.sleep(2)

#         # Kiểm tra kết quả trong bảng
#         table_text = driver.find_element(By.TAG_NAME, "table").text
#         print("Table content after filtering:", table_text)  # Debug statement
#         # Check for the date in the table
#         self.assertIn("Jan. 1, 2025", table_text, "Không tìm thấy ngày 2025-01-01 trong bảng kết quả.")
#         # Check for the status in the table
#         self.assertIn("pending", table_text, "Không tìm thấy trạng thái 'pending' trong bảng kết quả.")
        

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()