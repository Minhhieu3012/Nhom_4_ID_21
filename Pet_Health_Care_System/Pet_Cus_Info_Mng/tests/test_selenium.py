from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import time

# class AddCustomerAndPetTest(unittest.TestCase):
#     def setUp(self):
#         # Sử dụng Service để khởi tạo WebDriver
#         service = Service("D:/Tài Liệu Công Nghệ Phần Mềm/chromedriver-win64/chromedriver-win64/chromedriver.exe")
#         self.driver = webdriver.Chrome(service=service)
#         self.driver.get("http://127.0.0.1:8000/")  # URL danh sách khách hàng

#     def test_add_customer(self):
#         driver = self.driver

#         # Nhấn vào menu khách hàng
#         driver.find_element(By.LINK_TEXT, "KHÁCH HÀNG").click()
#         time.sleep(5)

#         # Nhấn nút thêm khách hàng
#         driver.find_element(By.LINK_TEXT, "THÊM KHÁCH HÀNG MỚI").click()
#         time.sleep(5)

#         # Điền thông tin khách hàng
#         lastName=driver.find_element(By.ID, "Họ")
#         lastName.send_keys("Alexandro")

#         firstName=driver.find_element(By.ID, "Tên")
#         firstName.send_keys("Garnacho")

#         email=driver.find_element(By.ID, "E-mail")
#         email.send_keys("gnc123@gmail.com")

#         age=driver.find_element(By.ID, "Tuổi")
#         age.send_keys("19")

#         phoneNumber=driver.find_element(By.ID, "Số điện thoại")
#         phoneNumber.send_keys("0327329948")

#         address=driver.find_element(By.ID, "Địa chỉ")
#         address.send_keys("47/24/38 bui dinh tuy")

#         gender=driver.find_element(By.ID, "Giới tính")
#         gender.send_keys("Nam")
#         time.sleep(4)

#         # Lưu khách hàng
#         submit_button = driver.find_element(By.LINK_TEXT, "TẠO KHÁCH HÀNG")
#         submit_button.click()

#         # Nhấn nút Hủy để quay lại danh sách khách hàng
#         cancel=driver.find_element(By.LINK_TEXT, "Hủy")
#         cancel.click()
#         print("Thêm khách hàng thành công.")

#         # Kiểm tra danh sách khách hàng
#         welcome_message = driver.find_element(By.ID, "welcome")
#         self.assertIn("Welcome", welcome_message.text)


    # def test_add_pet(self):
    #     driver = self.driver

    #     # Nhấn vào menu thú cưng
    #     driver.find_element(By.LINK_TEXT, "THÚ CƯNG").click()
    #     time.sleep(5)

    #     # Nhấn nút thêm thú cưng mới
    #     driver.find_element(By.LINK_TEXT, "THÊM THÚ CƯNG MỚI").click()
    #     time.sleep(5)

    #     # Nhập thông tin thú cưng
    #     driver.find_element(By.NAME, "name").send_keys("Buddy")
    #     driver.find_element(By.NAME, "dateOfBirth").send_keys("2022-02-12")
    #     driver.find_element(By.NAME, "species").send_keys("Chó")
    #     driver.find_element(By.NAME, "healthStatus").send_keys("Sức khỏe tốt")
    #     driver.find_element(By.NAME, "owner").send_keys("Garnacho")
    #     driver.find_element(By.NAME, "gender").send_keys("Đực")
    #     time.sleep(5)

    #     # Lưu thú cưng
    #     driver.find_element(By.XPATH, "//button[text()='Save']").click()
    #     time.sleep(5)

    #     # Nhấn nút Hủy để quay lại danh sách thú cưng
    #     driver.find_element(By.XPATH, "//button[text()='Cancel']").click()
    #     time.sleep(5) 
    #     print("Thêm thú cưng thành công.")

    #     # Kiểm tra danh sách thú cưng
    #     pet_list = driver.find_element(By.TAG_NAME, "body").text
    #     self.assertIn("Buddy", pet_list)
    #     print("Thú cưng mới đã xuất hiện trong danh sách.")

    
#     def tearDown(self):
#         # Đóng trình duyệt sau khi kiểm tra
#         self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()


class AddCustomerTest(unittest.TestCase):
    def setUp(self):
        # Khởi tạo WebDriver
        service = Service("D:/Tài Liệu Công Nghệ Phần Mềm/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://127.0.0.1:8000/customers")  # URL của trang danh sách khách hàng

    def test_add_customer(self):
        driver = self.driver
        
        # Nhấn nút "Thêm khách hàng mới"
        driver.find_element(By.LINK_TEXT, "THÊM KHÁCH HÀNG MỚI").click()
        time.sleep(2)

        # Nhập thông tin khách hàng
        driver.find_element(By.NAME, "firstName").send_keys("Garnacho")
        driver.find_element(By.NAME, "lastName").send_keys("Alexandro")
        driver.find_element(By.NAME, "email").send_keys("gnc123@gmail.com")
        driver.find_element(By.NAME, "phoneNumber").send_keys("0327329948")
        driver.find_element(By.NAME, "address").send_keys("47/24/38 bui dinh tuy")
        driver.find_element(By.NAME, "age").send_keys("19")
        driver.find_element(By.NAME, "gender").send_keys("Nam")
        time.sleep(2)

        # Nhấn nút "Tạo khách hàng"
        driver.find_element(By.XPATH, "//button[contains(.,'Tạo khách hàng')]").click()
        time.sleep(2)

        # Quay lại danh sách bằng cách nhấn nút "Hủy"
        driver.find_element(By.LINK_TEXT, "Hủy").click()
        time.sleep(2)

        # Kiểm tra khách hàng vừa tạo đã xuất hiện trong danh sách
        body_text = driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Garnacho Alexandro", body_text)
        print("Khách hàng mới đã được thêm thành công!")

    def tearDown(self):
        # Đóng trình duyệt sau khi chạy xong
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

