from django import forms

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