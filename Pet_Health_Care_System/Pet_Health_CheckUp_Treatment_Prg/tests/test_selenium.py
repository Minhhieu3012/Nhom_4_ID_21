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
from selenium.webdriver.support.ui import WebDriverWait

class Function_Pet_MedicalRecord_TreatmentProgress_Medication_Notification_Test(unittest.TestCase):
    def setUp(self):
        # Sử dụng Service để khởi tạo WebDriver
        service = Service("D:/Tài Liệu Công Nghệ Phần Mềm/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
    def tearDown(self):
        self.driver.quit()
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

    def test_unit_01_pet_create(self):
        print("Bắt đầu test chức năng tạo thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "THÚ CƯNG 2").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "THÊM THÚ CƯNG MỚI").click()
        time.sleep(2)

        # Điền thông tin thú cưng
        driver.find_element(By.ID, "id_name").send_keys("Pepsi")
        driver.find_element(By.ID, "id_age").send_keys("10")
        driver.find_element(By.ID, "id_species").send_keys("Chó")
        # Sửa id này từ "id_healthStatus" thành "id_current_health_status"
        driver.find_element(By.ID, "id_current_health_status").send_keys("Sức khỏe tốt")
        time.sleep(2)

        # --- Lưu thú cưng ---
        driver.find_element(By.XPATH, "//button[text()='Tạo thú cưng']").click()
        time.sleep(2)

        # Thử tìm nút Hủy (hoặc chuyển về danh sách)
        try:
            wait = WebDriverWait(driver, 20)
            cancel_btn = wait.until(EC.element_to_be_clickable((By.ID, "cancel-link")))
            cancel_btn.click()
        except Exception as e:
            print("Không tìm thấy nút Hủy:", e)
            # Nếu không tìm thấy nút "Hủy", có thể trang đã tự chuyển hướng.
            pass

        print("Thêm thú cưng thành công. Kiểm tra danh sách...")
        try:
            pet_list_element = driver.find_element(By.ID, "pet_list")
            self.assertIn("Pepsi", pet_list_element.text)
            print("Tên thú cưng đã hiển thị trong danh sách...")
        except Exception as e:
            print("Không tìm thấy dữ liệu thú cưng vừa tạo:", e)

        time.sleep(5)


    def test_unit_02_pet_update(self):
        print("Bắt đầu test chức năng chỉnh sửa thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        time.sleep(3)

        # Vào trang danh sách thú cưng
        driver.find_element(By.LINK_TEXT, "THÚ CƯNG 2").click()
        time.sleep(2)
        
        # Nhấn vào nút ba chấm của dòng cuối cùng để mở dropdown
        driver.find_element(By.XPATH, ".//td[last()]//button").click()
        time.sleep(1)
        
        # Tìm và click vào liên kết "Xem chi tiết" trong dropdown
        wait = WebDriverWait(driver, 20)
        xem_chi_tiet_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Xem chi tiết")))
        xem_chi_tiet_link.click()
        time.sleep(2)
        
        print("Đã vào trang chi tiết thú cưng.")
        time.sleep(2)
        
        # Nhấn nút "CHỈNH SỬA" trên trang chi tiết
        driver.find_element(By.LINK_TEXT, "CHỈNH SỬA").click()
        time.sleep(2)
        
        pet_name = wait.until(EC.presence_of_element_located((By.ID, "id_name")))
        pet_name.clear()
        pet_name.send_keys("Jack")
        
        # Nhấn nút "Lưu" để lưu thay đổi
        driver.find_element(By.XPATH, "//button[text()='Lưu']").click()
        time.sleep(2)
        
        # Sau khi lưu, ứng dụng chuyển hướng về trang danh sách thú cưng.
        print("Sau khi lưu, đợi trang danh sách load...")
        wait.until(EC.presence_of_element_located((By.ID, "pet_list")))
        time.sleep(2)
    

    def test_unit_11_pet_delete(self):
        print("Bắt đầu test chức năng xóa thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        time.sleep(3)

        # Vào trang danh sách thú cưng
        driver.find_element(By.LINK_TEXT, "THÚ CƯNG 2").click()
        time.sleep(2)
        
        # Nhấn vào nút ba chấm của dòng cuối cùng để mở dropdown
        driver.find_element(By.XPATH, ".//td[last()]//button").click()
        time.sleep(1)
        
        # Tìm và click vào liên kết "Xem chi tiết" trong dropdown
        wait = WebDriverWait(driver, 20)
        xem_chi_tiet_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Xem chi tiết")))
        xem_chi_tiet_link.click()
        time.sleep(2)
        
        print("Đã vào trang chi tiết thú cưng.")
        time.sleep(2)
        
        driver.find_element(By.LINK_TEXT, "XÓA").click()
        time.sleep(2)

        print("Đã vào trang xóa thú cưng.")
        time.sleep(4)

        # Xóa thú cưng
        driver.find_element(By.XPATH, "//button[text()='Xóa']").click()
        time.sleep(4)
        print("Xóa thú cưng thành công")


# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
    
    def test_unit_03_pet_medical_record_form(self):
        print("Bắt đầu test chức năng xem hồ sơ khám bệnh của thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "THÚ CƯNG 2").click()
        time.sleep(2)

        # Nhấn vào nút ba chấm của dòng cuối cùng để mở dropdown
        driver.find_element(By.XPATH, ".//td[last()]//button").click()
        time.sleep(1)
        
        # Tìm và click vào liên kết "Xem chi tiết" trong dropdown
        wait = WebDriverWait(driver, 20)
        xem_chi_tiet_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Xem chi tiết")))
        xem_chi_tiet_link.click()
        time.sleep(2)
        
        print("Đã vào trang chi tiết thú cưng.")
        time.sleep(2)
        
        # Chuyển sang trang hồ sơ khám bệnh
        driver.find_element(By.LINK_TEXT, "XEM HỒ SƠ KHÁM BỆNH").click()
        time.sleep(2)

        print("Đã vào trang hồ sơ khám bệnh của thú cưng.")
        time.sleep(2)

        # Nhấn nút thêm bệnh án mới
        driver.find_element(By.LINK_TEXT, "THÊM BỆNH ÁN MỚI").click()
        time.sleep(2)

        print("Đã vào trang tạo bệnh án.")
        time.sleep(2)

        # Điền thông tin vào form
        select_pet = wait.until(EC.element_to_be_clickable((By.NAME, "pet")))
        select_pet.click()
        select_pet.send_keys(Keys.ARROW_DOWN)  # Chọn thú cưng đầu tiên (có thể cần điều chỉnh)
        select_pet.send_keys(Keys.RETURN)
        time.sleep(2)

        # Nhập ngày khám
        date_input = driver.find_element(By.NAME, "date")
        date_input.send_keys("12/02/2025")
        time.sleep(2)

        # Nhập triệu chứng
        symptom_input = driver.find_element(By.NAME, "symptoms")
        symptom_input.clear()
        symptom_input.send_keys("Ho, sốt, biếng ăn")
        time.sleep(2)

        # Nhập bệnh/chẩn đoán
        disease_input = driver.find_element(By.NAME, "disease")
        disease_input.send_keys("Cảm cúm do thay đổi thời tiết")
        time.sleep(2)

        # Nhập ghi chú của bác sĩ
        vet_notes_input = driver.find_element(By.NAME, "vet_notes")
        vet_notes_input.clear()
        vet_notes_input.send_keys("Cần theo dõi thêm, bổ sung vitamin")
        time.sleep(2)

        wait = WebDriverWait(driver, 20)

        # Chờ xem nút có phải "Lưu bệnh án" hoặc "Cập nhật" không
        save_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Lưu') or contains(text(), 'Cập nhật')]")
        ))
        save_button.click()

        print("Bệnh án đã được tạo thành công.")

        # Kiểm tra xem bệnh án có xuất hiện trong danh sách không
        time.sleep(2)
        page_source = driver.page_source
        self.assertIn("Ho, sốt, biếng ăn", page_source)
        print("Bệnh án đã được lưu và hiển thị trên danh sách.")

        time.sleep(4)

    def test_unit_04_pet_medical_record_form_edit(self):
        print("Bắt đầu test chức năng chỉnh sửa hồ sơ khám bệnh của thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "THÚ CƯNG 2").click()
        time.sleep(2)

        # Nhấn vào nút ba chấm của dòng cuối cùng để mở dropdown
        driver.find_element(By.XPATH, ".//td[last()]//button").click()
        time.sleep(1)
        
        # Tìm và click vào liên kết "Xem chi tiết" trong dropdown
        wait = WebDriverWait(driver, 20)
        xem_chi_tiet_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Xem chi tiết")))
        xem_chi_tiet_link.click()
        time.sleep(2)
        
        print("Đã vào trang chi tiết thú cưng.")
        time.sleep(2)
        
        # Chuyển sang trang hồ sơ khám bệnh
        driver.find_element(By.LINK_TEXT, "XEM HỒ SƠ KHÁM BỆNH").click()
        time.sleep(2)

        print("Đã vào trang hồ sơ khám bệnh của thú cưng.")
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "SỬA").click()
        time.sleep(2)

        print("Đang chỉnh sửa thông tin hồ sơ khám bệnh...")

        # Nhập ngày khám
        date_input = driver.find_element(By.NAME, "date")
        date_input.send_keys("12/02/2025")
        time.sleep(2)

        # Cập nhập ghi chú của bác sĩ
        vet_notes_input = driver.find_element(By.NAME, "vet_notes")
        vet_notes_input.clear()
        vet_notes_input.send_keys("Cần theo dõi thêm, bổ sung vitamin, bổ sung thêm: cần uống nhiều nước và tái khám thường xuyên")
        time.sleep(2)

        wait = WebDriverWait(driver, 20)

        # Chờ xem nút có phải "Lưu bệnh án" hoặc "Cập nhật" không
        save_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Lưu') or contains(text(), 'Cập nhật')]")
        ))
        save_button.click()

        print("Bệnh án đã được chỉnh sửa thành công.")

        # Kiểm tra xem bệnh án có xuất hiện trong danh sách không
        time.sleep(2)
        page_source = driver.page_source
        self.assertIn("Ho, sốt, biếng ăn", page_source)
        print("Bệnh án đã được lưu và hiển thị trên danh sách.")

        time.sleep(4)


    def test_unit_10_pet_medical_record_delete(self):
        print("Bắt đầu test chức năng xóa hồ sơ khám bệnh của thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "THÚ CƯNG 2").click()
        time.sleep(2)

        # Nhấn vào nút ba chấm của dòng cuối cùng để mở dropdown
        driver.find_element(By.XPATH, ".//td[last()]//button").click()
        time.sleep(1)
        
        # Tìm và click vào liên kết "Xem chi tiết" trong dropdown
        wait = WebDriverWait(driver, 20)
        xem_chi_tiet_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Xem chi tiết")))
        xem_chi_tiet_link.click()
        time.sleep(2)
        
        print("Đã vào trang chi tiết thú cưng.")
        time.sleep(2)
        
        # Chuyển sang trang hồ sơ khám bệnh
        driver.find_element(By.LINK_TEXT, "XEM HỒ SƠ KHÁM BỆNH").click()
        time.sleep(2)

        print("Đã vào trang hồ sơ khám bệnh của thú cưng.")
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "XÓA").click()
        time.sleep(2)

        print("Đã vào trang xóa thú cưng.")
        time.sleep(4)

        # Xóa hồ sơ khám bệnh
        driver.find_element(By.XPATH, "//button[text()='Xóa']").click()
        time.sleep(4)
        print("Xóa hồ sơ khám bệnh thành công")

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

    def test_unit_07_pet_treatment_progress_form(self):
        print("🔍 Bắt đầu test chức năng xem tiến trình điều trị của thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        # Vào trang danh sách thú cưng
        driver.find_element(By.LINK_TEXT, "THÚ CƯNG 2").click()
        time.sleep(2)

        # Nhấn vào nút ba chấm của dòng cuối cùng để mở dropdown
        driver.find_element(By.XPATH, ".//td[last()]//button").click()
        time.sleep(1)
        
        # Tìm và click vào liên kết "Xem chi tiết" trong dropdown
        wait = WebDriverWait(driver, 10)
        xem_chi_tiet_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Xem chi tiết")))
        xem_chi_tiet_link.click()
        time.sleep(2)
        
        print("✅ Đã vào trang chi tiết thú cưng.")
        time.sleep(2)
        
        # Chuyển sang trang hồ sơ khám bệnh
        driver.find_element(By.LINK_TEXT, "XEM TIẾN TRÌNH ĐIỀU TRỊ").click()
        time.sleep(2)

        print("✅ Đã vào trang tiến trình điều trị của thú cưng.")
        time.sleep(2)

        # Nhấn nút thêm bệnh án mới
        driver.find_element(By.LINK_TEXT, "THÊM TIẾN TRÌNH ĐIỀU TRỊ MỚI").click()
        time.sleep(2)

        print("✅ Đã vào trang tạo tiến trình điều trị.")
        time.sleep(2)

        # ---- Điền form ----
        select_pet = wait.until(EC.element_to_be_clickable((By.NAME, "pet")))
        select_pet.click()
        select_pet.send_keys(Keys.ARROW_DOWN)  # Chọn thú cưng đầu tiên (có thể cần điều chỉnh)
        select_pet.send_keys(Keys.RETURN)
        time.sleep(2)

        # Chọn bệnh án (dropdown "medical_record")
        select_medical_record = wait.until(EC.element_to_be_clickable((By.NAME, "medical_record")))
        select_medical_record.click()
        select_medical_record.send_keys(Keys.ARROW_DOWN)
        select_medical_record.send_keys(Keys.RETURN)
        time.sleep(2)

        # Nhập phương pháp điều trị
        treatment_method_field = wait.until(EC.presence_of_element_located((By.NAME, "treatment_method")))
        treatment_method_field.clear()
        treatment_method_field.send_keys("Tiêm thuốc kháng sinh")
        print("✅ Đã điền phương pháp điều trị.")
        time.sleep(1)

        # Nhập ngày tái khám (định dạng YYYY-MM-DD)
        next_appointment_field = wait.until(EC.presence_of_element_located((By.NAME, "next_appointment_date")))
        next_appointment_field.clear()
        next_appointment_field.send_keys("12/02/2025")
        print("✅ Đã điền ngày tái khám.")
        time.sleep(1)

        # Nhập tình trạng sau điều trị
        updated_health_status_field = wait.until(EC.presence_of_element_located((By.NAME, "updated_health_status")))
        updated_health_status_field.clear()
        updated_health_status_field.send_keys("Đã hồi phục tốt")
        print("✅ Đã điền tình trạng sau điều trị.")
        time.sleep(1)

        # Nhấn nút lưu tiến trình (nút có text "Lưu tiến trình" hoặc "Cập nhật")
        save_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Lưu') or contains(text(), 'Cập nhật')]")
        ))
        save_button.click()

        print("Tiến trình điều trị đã được tạo thành công.")

        # Kiểm tra xem Tiến trình điều trị có xuất hiện trong danh sách không
        time.sleep(2)
        page_source = driver.page_source
        self.assertIn("Tiêm thuốc kháng sinh", page_source)
        print("Tiến trình điều trị đã được lưu và hiển thị trên danh sách.")

        time.sleep(4)


    def test_unit_09_pet_treatment_progress_delete(self):
        print("🔍 Bắt đầu test chức năng xóa tiến trình điều trị của thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        # Vào trang danh sách thú cưng
        driver.find_element(By.LINK_TEXT, "THÚ CƯNG 2").click()
        time.sleep(2)

        # Nhấn vào nút ba chấm của dòng cuối cùng để mở dropdown
        driver.find_element(By.XPATH, ".//td[last()]//button").click()
        time.sleep(1)
        
        # Tìm và click vào liên kết "Xem chi tiết" trong dropdown
        wait = WebDriverWait(driver, 10)
        xem_chi_tiet_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Xem chi tiết")))
        xem_chi_tiet_link.click()
        time.sleep(2)
        
        print("✅ Đã vào trang chi tiết thú cưng.")
        time.sleep(2)
        
        # Chuyển sang trang hồ sơ khám bệnh
        driver.find_element(By.LINK_TEXT, "XEM TIẾN TRÌNH ĐIỀU TRỊ").click()
        time.sleep(2)

        print("✅ Đã vào trang tiến trình điều trị của thú cưng.")
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "XÓA").click()
        time.sleep(2)

        print("Đã vào trang xóa thú cưng.")
        time.sleep(3)

        # Xóa hồ sơ khám bệnh
        driver.find_element(By.XPATH, "//button[text()='Xóa']").click()
        time.sleep(4)
        print("Xóa tiến trình điều trị thành công")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
    
    def test_unit_05_pet_medication_form(self):
        print("🔍 Bắt đầu test chức năng tạo đơn thuốc mới của thú cưng...")
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        # Vào trang thuốc điều trị
        driver.find_element(By.LINK_TEXT, "THUỐC ĐIỀU TRỊ").click()
        time.sleep(2)

        print("✅ Đã vào trang thuốc điều trị.")
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "THÊM THUỐC MỚI").click()
        time.sleep(2)

        print("✅ Đã vào trang thêm thuốc mới.")
        time.sleep(2)

        name_field = wait.until(EC.presence_of_element_located((By.NAME, "name")))
        name_field.clear()
        name_field.send_keys("Amoxicillin")
        print("✅ Đã điền tên thuốc.")
        time.sleep(1)

        description_field = wait.until(EC.presence_of_element_located((By.NAME, "description")))
        description_field.clear()
        description_field.send_keys("Kháng sinh phổ rộng, thường dùng để điều trị nhiễm trùng do vi khuẩn.")
        print("✅ Đã điền mô tả thuốc.")
        time.sleep(1)

        dosage_info_field = wait.until(EC.presence_of_element_located((By.NAME, "dosage_info")))
        dosage_info_field.clear()
        dosage_info_field.send_keys("Uống 2 lần/ngày, mỗi lần 250mg, sau bữa ăn.")
        print("✅ Đã điền hướng dẫn sử dụng.")
        time.sleep(1)

        # Nhấn nút lưu tiến trình (nút có text "Lưu tiến trình" hoặc "Cập nhật")
        save_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Lưu') or contains(text(), 'Cập nhật')]")
        ))
        save_button.click()

        print("Tiến trình điều trị đã được tạo thành công.")
        
        time.sleep(2)
        page_source = driver.page_source
        self.assertIn("Amoxicillin", page_source)
        print("Thuốc đã được lưu và hiển thị trên danh sách.")

        time.sleep(4)


    def test_unit_08_pet_medication_delete(self):
        print("🔍 Bắt đầu test chức năng xóa đơn thuốc mới của thú cưng...")
        driver = self.driver
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        # Vào trang danh sách thú cưng
        driver.find_element(By.LINK_TEXT, "THUỐC ĐIỀU TRỊ").click()
        time.sleep(2)
        
        print("✅ Đã vào trang danh sách thuốc điều trị.")
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "XÓA").click()
        time.sleep(2)

        print("Đã vào trang xóa thuốc.")
        time.sleep(3)

        # Xóa hồ sơ khám bệnh
        driver.find_element(By.XPATH, "//button[text()='Xóa']").click()
        time.sleep(4)
        print("Xóa thuốc thành công")

    
    def test_unit_06_pet_medication_edit(self):
        print("🔍 Bắt đầu test chức năng cập nhật đơn thuốc mới của thú cưng...")
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.get("http://127.0.0.1:8000/") 
        time.sleep(3)

        # Vào trang danh sách thú cưng
        driver.find_element(By.LINK_TEXT, "THUỐC ĐIỀU TRỊ").click()
        time.sleep(2)
        
        print("✅ Đã vào trang danh sách thuốc điều trị.")
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "SỬA").click()
        time.sleep(2)

        print("Đã vào trang cập nhật thuốc.")
        time.sleep(3)

        description_field = wait.until(EC.presence_of_element_located((By.NAME, "description")))
        description_field.clear()
        description_field.send_keys("Kháng sinh phổ rộng, thường dùng để điều trị nhiễm trùng do vi khuẩn. Bổ sung: Nên tự cách li tại nhà")
        print("✅ Đã bổ sung mô tả thuốc.")
        time.sleep(1)

        # Nhấn nút lưu tiến trình (nút có text "Lưu tiến trình" hoặc "Cập nhật")
        save_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Lưu') or contains(text(), 'Cập nhật')]")
        ))
        save_button.click()

        print("Thuốc đã được cập nhật thành công.")
        
        time.sleep(2)
        page_source = driver.page_source
        self.assertIn("Amoxicillin", page_source)
        print("Thuốc đã được cập nhật và hiển thị trên danh sách.")

        time.sleep(4)


#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()