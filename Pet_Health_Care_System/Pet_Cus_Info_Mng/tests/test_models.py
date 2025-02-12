#------------------
#Unit Testing
#------------------
from django.test import TestCase, Client
from django.urls import reverse
from Pet_Cus_Info_Mng.models import Pet, Customer, MedicalRecord, Appointment

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.customer = Customer.objects.create(
            firstName="Alexandro", 
            lastName="Garnacho", 
            email="grn123@gmail.com", 
            phoneNumber="0327329948",
            address="47/24/38 Bùi Đình Túy", 
            age=19, 
            gender="Nam"
        )
        self.pet = Pet.objects.create(
            name="Buddy", 
            species="Bull Pháp", 
            gender="Đực", 
            dateOfBirth="2022-02-22", 
            healthStatus="Sức khỏe tốt", 
            owner=self.customer
        )
        self.medicalRecord = MedicalRecord.objects.create(
            pet = self.pet,
            date="2023-02-22",      
            treatmentDetails="Khám sức khỏe định kỳ và tiêm vaccine",
            doctor="Bác sĩ Nguyễn Văn A",
            remarks="Cần theo dõi thêm phần hô hấp"
        )
        self.appointment = Appointment.objects.create(
            customer = self.customer,
            pet = self.pet,
            date="2024-02-22",
            time = "10:00:00",
            status = "Đã thanh toán"
        )
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

    def test_home_view(self):
        response = self.client.get(reverse('app_admin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_admin/app_admin.html')
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
    def test_pets_view(self):
        response = self.client.get(reverse('pet_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pet.name)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/pets.html')

    def test_pet_new_view(self):
        response = self.client.get(reverse('pet_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/pet_form.html')

    def test_edit_pet_view(self):
        response = self.client.get(reverse('pet_edit', args=[self.pet.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pet.name)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/pet_edit.html')

    def test_delete_pet_view(self):
        response = self.client.get(reverse('pet_delete', args=[self.pet.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pet.name)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/pet_delete.html')
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

    def test_customers_view(self):
        response = self.client.get(reverse('customer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.customer.firstName)
        self.assertContains(response, self.customer.lastName)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/customers.html')

    def test_customer_new_view(self):
        response = self.client.get(reverse('customer_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/customer_form.html')

    def test_customer_edit_view(self):
        response = self.client.get(reverse('customer_edit', args=[self.customer.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.customer.firstName)
        self.assertContains(response, self.customer.lastName)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/customer_edit.html')

    def test_customer_delete_view(self):
        response = self.client.get(reverse('customer_delete', args=[self.customer.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.customer.firstName)
        self.assertContains(response, self.customer.lastName)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/customer_delete.html')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

    def test_appointment_view(self):
        response = self.client.get(reverse('appointments_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.customer.firstName)
        self.assertContains(response, self.customer.lastName)
        self.assertContains(response, self.pet.name)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/appointments-list.html')
    
    def test_appointment_create_view(self):
        response = self.client.get(reverse('appointments_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/appointments-create.html')
    
    def test_appointment_filter_view(self):
        response = self.client.get(reverse('appointments_filter'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.appointment.status)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/appointments-filter.html')

    def test_appointments_history_view(self):
        response = self.client.get(reverse('appointments_history', args=[self.customer.email]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.customer.email)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/appointments-history.html')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

    def test_medical_records_history_view(self):
        url = reverse('medicalRecords_history', args=[self.pet.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.medicalRecord.treatmentDetails)
        self.assertContains(response, self.medicalRecord.doctor)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/medicalRecords-history.html')
        