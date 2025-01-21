from django import forms
from .models import Pet, Customer

class CustomerForm(forms.Form):
    lastName = forms.CharField(label="lastName", max_length=100)
    firstName = forms.CharField(label="firstName", max_length=100)
    email = forms.EmailField(label="E-mail", max_length=255)
    phoneNumber = forms.CharField(label="phoneNumber", max_length=15)
    address = forms.CharField(label="address", max_length=255)
    age = forms.IntegerField(label="age")
    gender = forms.ChoiceField(
        label="gender",
        choices=[("Nam", "Nam"), ("Nữ", "Nữ"), ("LGBT", "LGBT")]
    )

class PetForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)  
    species = forms.CharField(label="species", max_length=50)  
    gender = forms.ChoiceField(
        label="gender",
        choices=[("Đực", "Đực"), ("Cái", "Cái")],  # Lựa chọn giới tính
    )
    dateOfBirth = forms.DateField(
        label="dateOfBirht",
        widget=forms.DateInput(attrs={"type": "date"}), 
    )
    age = forms.IntegerField(
        label="age",
        required=False,
    )
    healthStatus = forms.ChoiceField(
        label="healthStatus",
        choices=[
            ('Đang nhập viện', 'Đang nhập viện'),
            ('Đang điều trị ngoại trú', 'Đang điều trị ngoại trú'),
            ('Đã xuất viện', 'Đã xuất viện'),
            ('Sức khỏe tốt','Sức khỏe tốt'),
            ('Cần tiêm phòng','Cần tiêm phòng'),
            ('Béo phì','Béo phì'),
            ('Bị chấn thương','Bị chấn thương'),
            ('Dinh dưỡng kém','Dinh dưỡng kém'),
            ('Giai đoạn cuối','Giai đoạn cuối'),
        ], 
    )
    owner = forms.ChoiceField(
        label="owner",
        choices=[]
    )

class MedicalRecordsForm(forms.Form):
    pet = forms.ChoiceField(
        label="Pet",
        choices=[],
        required=True
    )
    date = forms.DateField(label="Date", widget=forms.DateInput(attrs={'type': 'date'}))
    treatmentDetails = forms.CharField(
        label="Treatment Details",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=True
    )
    doctor = forms.CharField(label="Doctor", max_length=255, required=True)
    remarks = forms.CharField(
        label="Remarks",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )
    # Khởi tạo để thêm choices cho trường pet
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pet'].choices = [(pet.id, pet.name) for pet in Pet.objects.all()]


class AppointmentsForm(forms.Form):
    customer = forms.ChoiceField(label="Customer", choices=[], required=True)
    pet = forms.ChoiceField(label="Pet", choices=[], required=True)
    date = forms.DateField(label="Date", widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(label="Time", widget=forms.TimeInput(attrs={'type': 'time'}))
    status = forms.ChoiceField(
        label="Status",
        choices=[('pending', 'Đang chờ xử lý'), ('completed', 'Đã hoàn thành')],
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Sử dụng id làm giá trị và họ tên làm nhãn
        self.fields['customer'].choices = [(customer.id, f"{customer.lastName} {customer.firstName}") for customer in Customer.objects.all()]
        self.fields['pet'].choices = [(pet.id, pet.name) for pet in Pet.objects.all()]

class TransactionForm(forms.Form):
    customer = forms.ChoiceField(
        label="customer",
        choices=[],
        required=True
    )
    pet = forms.ChoiceField(
        label="pet",
        choices=[],
        required=True
    )
    service = forms.CharField(
        label="service",
        max_length=255,
        required=True
    )
    amount = forms.DecimalField(
        label="amount",
        max_digits=10,
        decimal_places=2,
        required=True
    )
    status = forms.ChoiceField(
        label="status",
        choices=[
            ('pending', 'Đang chờ xử lý'),
            ('completed', 'Đã hoàn thành'),
            ('failed', 'Thất bại'),
        ],
        required=True
    )
    remarks = forms.CharField(
        label="remarks",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].choices = [(customer.lastName, customer.firstName) for customer in Customer.objects.all()]
        self.fields['pet'].choices = [(pet.id, pet.name) for pet in Pet.objects.all()]

