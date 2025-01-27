# #------------------------------------------------------------------------------------------
# # Đây là file thử nghiệm. Toàn bộ test chính thức đã được chuyển sang thư mục AutoTest.
# #------------------------------------------------------------------------------------------

# import unittest
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# # Nếu có nhu cầu chờ đợi phần tử, import thêm:
# # from selenium.webdriver.support.wait import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC

# class Function_Customer_Pet_Appointment_Test(unittest.TestCase):
#     def setUp(self):
#         # Khởi tạo WebDriver (điều chỉnh đường dẫn chromedriver của bạn)
#         service = Service("D:/Tài Liệu Công Nghệ Phần Mềm/chromedriver-win64/chromedriver.exe")
#         self.driver = webdriver.Chrome(service=service)
#         self.driver.maximize_window()

#     def tearDown(self):
#         self.driver.quit()

#     # --------------------------------------------------------------------------
#     # 1. Test thêm lịch hẹn (Add Appointment)
#     # --------------------------------------------------------------------------
#     def test_add_appointment(self):
#         """
#         - Vào trang chủ
#         - Click "LỊCH HẸN"
#         - Click "THÊM LỊCH HẸN MỚI"
#         - Điền thông tin lịch hẹn
#         - Lưu
#         - Kiểm tra xem đã chuyển trang hoặc có hiển thị lịch hẹn vừa thêm
#         """
#         driver = self.driver
#         driver.get("http://127.0.0.1:8000/")  # URL trang chủ
#         time.sleep(2)

#         # Đi đến trang Lịch Hẹn
#         driver.find_element(By.LINK_TEXT, "LỊCH HẸN").click()
#         time.sleep(2)

#         # Thêm lịch hẹn mới
#         driver.find_element(By.LINK_TEXT, "THÊM LỊCH HẸN MỚI").click()
#         time.sleep(2)

#         # Chọn Khách hàng
#         select_customer = Select(driver.find_element(By.ID, "id_customer"))
#         # Ví dụ: chọn khách hàng theo thứ tự (index)
#         select_customer.select_by_index(1)
#         time.sleep(1)

#         # Chọn Pet
#         select_pet = Select(driver.find_element(By.ID, "id_pet"))
#         select_pet.select_by_index(1)
#         time.sleep(1)

#         # Nhập Date
#         driver.find_element(By.ID, "id_date").send_keys("2025-01-01")
#         time.sleep(1)

#         # Nhập Time
#         driver.find_element(By.ID, "id_time").send_keys("10:30")
#         time.sleep(1)

#         # Chọn Status
#         select_status = Select(driver.find_element(By.ID, "id_status"))
#         select_status.select_by_value("pending")  # "pending" hoặc "completed"

#         # Click nút "Lưu lịch hẹn"
#         driver.find_element(By.XPATH, "//button[text()='Lưu lịch hẹn']").click()
#         time.sleep(2)

#         # Kiểm tra xem trang có chuyển và hiển thị danh sách lịch hẹn
#         page_source = driver.page_source
#         self.assertIn("Lịch Hẹn", page_source, "Không thấy từ khóa 'Lịch Hẹn' trong trang sau khi lưu.")
#         # Bạn có thể kiểm tra thêm thông tin như ngày "2025-01-01" hiển thị không:
#         # self.assertIn("2025-01-01", page_source, "Không thấy ngày 2025-01-01 trong danh sách sau khi thêm.")

#     # --------------------------------------------------------------------------
#     # 2. Test lọc lịch hẹn (Filter Appointment)
#     # --------------------------------------------------------------------------
#     def test_filter_appointment(self):
#         """
#         - Vào trang Lịch hẹn (có form lọc)
#         - Nhập date + status
#         - Click 'Lọc'
#         - Kiểm tra kết quả
#         """
#         driver = self.driver
#         # Giả sử trang danh sách lịch hẹn và form lọc ở URL này:
#         driver.get("http://127.0.0.1:8000/appointments/")
#         time.sleep(2)

#         # Nhập date
#         driver.find_element(By.ID, "date").send_keys("2025-01-01")
#         time.sleep(1)

#         # Chọn status = "pending"
#         select_filter_status = Select(driver.find_element(By.ID, "status"))
#         select_filter_status.select_by_value("pending")
#         time.sleep(1)

#         # Click nút Lọc
#         driver.find_element(By.XPATH, "//button[text()='Lọc']").click()
#         time.sleep(2)

#         # Kiểm tra kết quả trong bảng
#         table_text = driver.find_element(By.TAG_NAME, "table").text
#         self.assertIn("2025-01-01", table_text, "Không tìm thấy ngày 2025-01-01 trong bảng kết quả.")
#         self.assertIn("Chưa thanh toán", table_text, "Không tìm thấy trạng thái 'Chưa thanh toán' trong bảng kết quả.")

#     # --------------------------------------------------------------------------
#     # 3. Test xóa lịch hẹn (Delete Appointment)
#     # --------------------------------------------------------------------------
#     def test_delete_appointment(self):
#         """
#         - Vào trang danh sách lịch hẹn
#         - Click 'XÓA' trên một lịch hẹn
#         - Xác nhận xóa (nếu có dialog)
#         - Kiểm tra lịch hẹn đã bị xóa khỏi danh sách
#         """
#         driver = self.driver
#         driver.get("http://127.0.0.1:8000/appointments/")
#         time.sleep(2)

#         # Giả sử có link text "XÓA" (hoặc "DELETE") bên cạnh lịch hẹn
#         driver.find_element(By.LINK_TEXT, "XÓA").click()
#         time.sleep(2)

#         # Nếu có alert xác nhận thì:
#         # driver.switch_to.alert.accept()
#         # time.sleep(2)

#         # Kiểm tra xem lịch hẹn đã bị xóa chưa. Ví dụ, kiểm tra ngày 2025-01-01 không còn trong trang:
#         page_source = driver.page_source
#         self.assertNotIn("2025-01-01", page_source, "Lịch hẹn vẫn hiển thị sau khi xóa.")

# if __name__ == "__main__":
#     unittest.main()
