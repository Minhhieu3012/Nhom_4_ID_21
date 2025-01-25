#------------------------------------------------------------------------------------------
# Đây là file thử nghiệm. Toàn bộ test chính thức đã được chuyển sang thư mục AutoTest.
#------------------------------------------------------------------------------------------

# from django.test import TestCase, Client
# from django.urls import reverse
# from app_admin.models import Course, Student

# class ViewsTestCase(TestCase):
#   def setUp(self):
#     self.client = Client()
#     self.course = Course.objects.create(name="Test Course")
#     self.student = Student.objects.create(name="Test Student")

#   def test_home_view(self):
#     response = self.client.get(reverse('home'))
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'home.html')

#   def test_courses_view(self):
#     response = self.client.get(reverse('courses'))
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'app_home/course/courses.html')
#     self.assertContains(response, self.course.name)

#   def test_edit_course_view(self):
#     response = self.client.get(reverse('edit_course', args=[self.course.id]))
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'app_home/course/course-edit.html')
#     self.assertContains(response, self.course.name)

#   def test_delete_course_view(self):
#     response = self.client.get(reverse('delete_course', args=[self.course.id]))
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'app_home/course/course-delete.html')
#     self.assertContains(response, self.course.name)

#   def test_students_view(self):
#     response = self.client.get(reverse('students'))
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'app_home/student/students.html')
#     self.assertContains(response, self.student.name)

#   def test_student_edit_view(self):
#     response = self.client.get(reverse('studentEdit', args=[self.student.id]))
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'app_home/student/student-edit.html')
#     self.assertContains(response, self.student.name)

#   def test_student_delete_view(self):
#     response = self.client.get(reverse('studentDelete', args=[self.student.id]))
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'app_home/student/student-delete.html')
#     self.assertContains(response, self.student.name)

#   def test_student_new_view(self):
#     response = self.client.get(reverse('studentNew'))
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'app_home/student/student-new.html')

#   def test_course_new_view(self):
#     response = self.client.get(reverse('CourseNew'))
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'app_home/course/course-new.html')

#----------------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import unittest

# class LoginTest(unittest.TestCase):
#     def setUp(self):
#         Setup the WebDriver (Chrome in this example)
#         self.driver = webdriver.Chrome()
#         self.driver.get("https://example.com/login")

#     def test_valid_login(self):
#         driver = self.driver
#         Find elements and perform actions
#         username = driver.find_element(By.ID, "username")
#         password = driver.find_element(By.ID, "password")
#         submit_button = driver.find_element(By.ID, "submit")

#         Input valid credentials and submit
#         username.send_keys("valid_user")
#         password.send_keys("valid_password")
#         submit_button.click()

#         Assert expected outcome (e.g., redirection or welcome message)
#         welcome_message = driver.find_element(By.ID, "welcome")
#         self.assertIn("Welcome", welcome_message.text)

#     def tearDown(self):
#         Close the browser
#         self.driver.quit()

# if _name_ == "__main__":
#     unittest.main()
#-------------------------------------------------------------------------------------------------

# from selenium import webdriver
# from django.test import LiveServerTestCase
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# class PetManagementSeleniumTest(LiveServerTestCase):
#     def setUp(self):
#         self.browser = webdriver.Chrome(executable_path="path/to/chromedriver")

#     def tearDown(self):
#         self.browser.quit()

#     def test_add_pet(self):
#         self.browser.get(f"{self.live_server_url}/add-pet/")
#         name_input = self.browser.find_element(By.NAME, "name")
#         age_input = self.browser.find_element(By.NAME, "age")
#         breed_input = self.browser.find_element(By.NAME, "breed")
#         owner_input = self.browser.find_element(By.NAME, "owner")

#         # Nhập dữ liệu
#         name_input.send_keys("Buddy")
#         age_input.send_keys("2")
#         breed_input.send_keys("Golden Retriever")
#         owner_input.send_keys("1")
#         self.browser.find_element(By.ID, "submit").click()

#         # Kiểm tra kết quả
#         self.assertIn("Pet added successfully", self.browser.page_source)