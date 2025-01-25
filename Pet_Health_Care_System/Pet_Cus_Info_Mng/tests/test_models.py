from django.test import TestCase, Client
from django.urls import reverse
from Pet_Cus_Info_Mng.models import Pet, Customer

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


    def test_home_view(self):
        response = self.client.get(reverse('app_admin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_admin/app_admin.html')

    def test_pets_view(self):
        response = self.client.get(reverse('pet_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/pets.html')
        self.assertContains(response, self.pet.name)

    def test_edit_pet_view(self):
        response = self.client.get(reverse('pet_edit', args=[self.pet.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/pet_edit.html')
        self.assertContains(response, self.pet.name)

    def test_delete_pet_view(self):
        response = self.client.get(reverse('pet_delete', args=[self.pet.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/pet_delete.html')
        self.assertContains(response, self.pet.name)

    def test_customers_view(self):
        response = self.client.get(reverse('customer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/customers.html')
        self.assertContains(response, self.customer.firstName)

    def test_customer_edit_view(self):
        response = self.client.get(reverse('customer_edit', args=[self.customer.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/customer_edit.html')
        self.assertContains(response, self.customer.firstName)

    def test_customer_delete_view(self):
        response = self.client.get(reverse('customer_delete', args=[self.customer.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/customer_delete.html')
        self.assertContains(response, self.customer.firstName)

    def test_customer_new_view(self):
        response = self.client.get(reverse('customer_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/customer_form.html')

    def test_pet_new_view(self):
        response = self.client.get(reverse('pet_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Pet_Cus_Info_Mng/pet_form.html')
