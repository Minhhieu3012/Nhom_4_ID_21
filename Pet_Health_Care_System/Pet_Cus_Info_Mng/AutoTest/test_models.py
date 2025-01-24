from django.test import TestCase
from Pet_Cus_Info_Mng.models import Pet, Customer
from datetime import date

class PetModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(firstName="Alexandro",lastName="Garnacho", email="grn123@gmail.com", age=19)
        # Tạo thú cưng
        self.pet = Pet.objects.create(
            name="Buddy",
            dateOfBirth=date(2022, 2, 22),  # Sử dụng dateOfBirth
            species="Bull Pháp",
            gender="Đực",
            healthStatus="Sức khỏe tốt",
            owner=self.customer,
        )
    def test_create_pet(self):
        self.assertEqual(self.pet.name, "Buddy")
        self.assertEqual(self.pet.owner, self.customer)
    def test_calculate_age(self):
        # Kiểm tra tuổi được tính chính xác
        calculated_age = self.pet.calculate_age()  # Hàm tự tính toán tuổi
        self.assertIsNotNone(calculated_age)
    def test_update_pet(self):
        self.pet.name="Max"
        self.pet.save()
        update_pet=Pet.objects.get(id=self.pet.id)
        self.assertEqual(update_pet.name, "Max")
    def test_delete_pet(self):
        pet_id=self.pet.id
        self.pet.delete()
        with self.assertRaises(Pet.DoesNotExist):
            Pet.objects.get(id=pet_id)