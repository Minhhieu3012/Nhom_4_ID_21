from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Đường dẫn chính xác tới file chromedriver.exe
service = Service("D:/Tài Liệu Công Nghệ Phần Mềm/chromedriver-win64/chromedriver-win64/chromedriver.exe")

# Khởi chạy trình duyệt Chrome
driver = webdriver.Chrome(service=service)

# Mở trang web kiểm tra
driver.get('https://google.com')
print(driver.title)

# Đóng trình duyệt
driver.quit()
