# views.py
from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import MedicalRecord, TreatmentProgress, Medication, Pet
from .forms import MedicalRecordForm, TreatmentProgressForm, MedicationForm, PetForm



#----------------------------
# --- Views cho Pet ---------
#----------------------------
class PetListView(ListView):
    model = Pet
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/pet_list.html'  
    context_object_name = 'pets'

class PetDetailView(DetailView):
    model = Pet
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/pet_detail.html'
    context_object_name = 'pet'

class PetCreateView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/pet_create.html'
    success_url = reverse_lazy('pet_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Thú cưng đã được tạo thành công!")
        return response

class PetUpdateView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/pet_update.html'
    success_url = reverse_lazy('pet_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Thông tin thú cưng đã được cập nhật thành công!")
        return response

class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/pet_delete.html'
    success_url = reverse_lazy('pet_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Thú cưng đã được xóa thành công!")
        return super().delete(request, *args, **kwargs)
    

# ----------------------------------------------
# Views cho Medical Record (Quản lý bệnh án)
# ----------------------------------------------
class MedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/medical_record_list.html' 
    context_object_name = 'medical_records'

    def get_queryset(self):
        # Nếu truyền pet_id qua URL, chỉ lấy bệnh án của thú cưng đó
        pet_id = self.kwargs.get('pet_id')
        if pet_id:
            return MedicalRecord.objects.filter(pet__id=pet_id).order_by('-date')
        return MedicalRecord.objects.all().order_by('-date')




class MedicalRecordCreateView(CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/medical_record_form.html'
    
    def form_valid(self, form):
        # Lấy pet_id từ URL
        pet_id = self.kwargs.get('pet_id')
        if pet_id:
            form.instance.pet_id = pet_id  # gán trực tiếp pet_id cho đối tượng
        else:
            if not form.cleaned_data.get('pet'):
                form.add_error('pet', 'Bạn phải chọn thú cưng.')
                return self.form_invalid(form)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # In ra lỗi để debug
        print("Form errors:", form.errors)
        return super().form_invalid(form)
    
    def get_success_url(self):
        # Sau khi lưu, self.object.pet.id phải có giá trị hợp lệ
        return reverse_lazy('medical_record_list', kwargs={'pet_id': self.object.pet.id})

class MedicalRecordUpdateView(UpdateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/medical_record_form.html'
    success_url = reverse_lazy('medical_record_list')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Bệnh án đã được cập nhật thành công!")
        return HttpResponseRedirect(self.get_success_url())


class MedicalRecordDeleteView(DeleteView):
    model = MedicalRecord
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/medical_record_delete.html'
    success_url = reverse_lazy('medical_record_list')

    def get_success_url(self):
        # Sử dụng self.object.pet.id để lấy pet_id của bệnh án vừa xóa
        return reverse_lazy('medical_record_list', kwargs={'pet_id': self.object.pet.id})


# ----------------------------------------------
# Views cho Treatment Progress (Tiến trình điều trị)
# ----------------------------------------------
class TreatmentProgressListView(ListView):
    model = TreatmentProgress
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/treatment_progress_list.html'
    context_object_name = 'treatment_progress_list'

    def get_queryset(self):
        pet_id = self.kwargs.get('pet_id')
        if pet_id:
            return TreatmentProgress.objects.filter(pet__id=pet_id).order_by('-updated_at')
        return TreatmentProgress.objects.all().order_by('-updated_at')


class TreatmentProgressCreateView(CreateView):
    model = TreatmentProgress
    form_class = TreatmentProgressForm
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/treatment_progress_form.html'
    success_url = reverse_lazy('treatment_progress_list')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Tiến trình điều trị đã được tạo thành công!")
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Truyền thêm danh sách bệnh án (nếu cần) để lựa chọn trong form
        context['medical_records'] = MedicalRecord.objects.all()
        return context


class TreatmentProgressUpdateView(UpdateView):
    model = TreatmentProgress
    form_class = TreatmentProgressForm
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/treatment_progress_form.html'
    success_url = reverse_lazy('treatment_progress_list')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Tiến trình điều trị đã được cập nhật thành công!")
        return HttpResponseRedirect(self.get_success_url())


class TreatmentProgressDeleteView(DeleteView):
    model = TreatmentProgress
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/treatment_progress_confirm_delete.html'
    success_url = reverse_lazy('treatment_progress_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Tiến trình điều trị đã được xóa thành công!")
        return super().delete(request, *args, **kwargs)


# ----------------------------------------------
# Views cho Medication (Quản lý thuốc)
# ----------------------------------------------
class MedicationListView(ListView):
    model = Medication
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/medication_list.html'
    context_object_name = 'medications'


class MedicationCreateView(CreateView):
    model = Medication
    form_class = MedicationForm
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/medication_form.html'
    success_url = reverse_lazy('medication_list')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thuốc đã được thêm thành công!")
        return HttpResponseRedirect(self.get_success_url())


class MedicationUpdateView(UpdateView):
    model = Medication
    form_class = MedicationForm
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/medication_form.html'
    success_url = reverse_lazy('medication_list')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thông tin thuốc đã được cập nhật thành công!")
        return HttpResponseRedirect(self.get_success_url())


class MedicationDeleteView(DeleteView):
    model = Medication
    template_name = 'Pet_Health_CheckUp_Treatment_Prg/medication_confirm_delete.html'
    success_url = reverse_lazy('medication_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Thuốc đã được xóa thành công!")
        return super().delete(request, *args, **kwargs)
