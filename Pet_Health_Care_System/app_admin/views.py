from datetime import datetime
from django.contrib import messages
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Admission, Pet, Room, Invoice
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import now



def pet(request):
    return HttpResponse("Hello world!")
def owner(request):
    return HttpResponse("Hello world!")
def room(request):
    return HttpResponse("Hello world!")
def admission(request):
    return HttpResponse("Hello world!")
def staff(request):
    return HttpResponse("Hello world!")
def invoice(request):
    return HttpResponse("Hello world!")
def app_admin(request):
    return render (request, 'home.html')

def rooms(request):
    #rooms = Room.objects.all()
    rooms = Room.objects.all()
    template = loader.get_template('app_admin/rooms.html')
    context = {
        'room' : rooms, 
    }
    return HttpResponse(template.render(context, request))

def room_edit(request, id):


    room = get_object_or_404(Room, id=id)

    if request.method == "POST":
        room.room_type = request.POST.get("room_type")
        room.capacity = request.POST.get("capacity")
        room.status = request.POST.get("status")
        room.save()
        return redirect("rooms")  # Chuyển hướng về danh sách rooms sau khi chỉnh sửa

    template = loader.get_template("app_admin/room-edit.html")
    context = {
        "room": room,
    }
    return HttpResponse(template.render(context, request))

def room_add(request):
    if request.method == "POST":
        room_type = request.POST.get("room_type")
        capacity = request.POST.get("capacity")
        status = request.POST.get("status")
        try:
            capacity = int(capacity)  # Chuyển đổi capacity sang số nguyên
            if capacity <= 0:
                messages.error(request, "Sức chứa phải là số dương.")
                return redirect("room-add")
            if capacity > 50:  # Giới hạn số lớn tùy ý (ví dụ: 50)
                messages.error(request, "Sức chứa không thể vượt quá 50.")
                return redirect("room-add")
            
        except ValueError:
            messages.error(request, "Vui lòng nhập một số hợp lệ cho sức chứa.")
            return redirect("room-add")

        Room.objects.create(room_type=room_type, capacity=capacity, status=status)

        return redirect("rooms")  # Chuyển hướng về danh sách phòng sau khi thêm

    return render(request, "app_admin/room-add.html")


def room_delete(request, id):
    # Lấy phòng từ database, nếu không tìm thấy thì trả về lỗi 404
    room = get_object_or_404(Room, id=id)

    # Xóa phòng
    room.delete()

    # Chuyển hướng về trang danh sách phòng sau khi xóa
    return redirect('rooms')

# *** QUẢN LÍ NHẬP VIỆN ***

# Hiển thị danh sách nhập viện
def admission_list(request):
    admissions = Admission.objects.all()
    return render(request, "app_admin/admission-list.html", {"admissions": admissions})


from django.db import models  # Import đúng models.F


# def admission_create(request):
#     if request.method == "POST":
#         pet_id = request.POST.get("pet")
#         room_id = request.POST.get("room")
#         admission_date = request.POST.get("admission_date")
#         discharge_date = request.POST.get("discharge_date")

#         pet = get_object_or_404(Pet, id=pet_id)
#         room = get_object_or_404(Room, id=room_id)

#         # Kiểm tra nếu phòng đã đầy
#         if room.current_occupancy >= room.capacity:
#             messages.error(request, "Room is already full!")
#             return redirect("admission-create")
        
#         # Chuyển đổi admission_date và discharge_date sang kiểu datetime
#         if admission_date:
#             admission_date = datetime.strptime(admission_date, "%Y-%m-%dT%H:%M")

#         if discharge_date:
#             discharge_date = datetime.strptime(discharge_date, "%Y-%m-%dT%H:%M")
#             # Kiểm tra nếu discharge_date nhỏ hơn admission_date
#             if discharge_date < admission_date:
#                 messages.error(request, "Ngày xuất viện không thể trước ngày nhập viện!")
#                 return redirect("admission-create")

#         # Tạo Admission
#         admission = Admission.objects.create(
#             pet=pet,
#             room=room,
#             admission_date=admission_date,
#             discharge_date=discharge_date if discharge_date else None
#         )

#         # Tăng số lượng thú cưng trong phòng
#         room.current_occupancy += 1
#         room.update_status()
#         room.save()  # Cần lưu sau khi cập nhật trạng thái

#         return redirect("admission-list")

#     pets = Pet.objects.all()
#     rooms = Room.objects.filter(current_occupancy__lt=models.F('capacity'))  # Chỉ hiển thị phòng chưa đầy
#     return render(request, "app_admin/admission-create.html", {"pets": pets, "rooms": rooms})

def admission_create(request):
    if request.method == "POST":
        pet_id = request.POST.get("pet")
        room_id = request.POST.get("room")
        admission_date = request.POST.get("admission_date")
        discharge_date = request.POST.get("discharge_date")

        pet = get_object_or_404(Pet, id=pet_id)
        room = get_object_or_404(Room, id=room_id)

        # Kiểm tra nếu phòng đã đầy
        if room.current_occupancy >= room.capacity:
            messages.error(request, "Room is already full!")
            return redirect("admission-create")

        # Kiểm tra định dạng ngày hợp lệ
        try:
            admission_date = datetime.strptime(admission_date, "%Y-%m-%dT%H:%M")

            # Kiểm tra nếu năm nhập viện có nhiều hơn 4 chữ số
            if admission_date.year > 9999:
                messages.error(request, "Định dạng ngày nhập viện không hợp lệ!")
                return redirect("admission-create")

        except ValueError:
            messages.error(request, "Vui lòng nhập đúng định dạng ngày!")
            return redirect("admission-create")

        if discharge_date:
            try:
                discharge_date = datetime.strptime(discharge_date, "%Y-%m-%dT%H:%M")

                # Kiểm tra ngày xuất viện phải sau ngày nhập viện
                if discharge_date < admission_date:
                    messages.error(request, "Ngày xuất viện không thể trước ngày nhập viện!")
                    return redirect("admission-create")

            except ValueError:
                messages.error(request, "Vui lòng nhập đúng định dạng ngày xuất viện!")
                return redirect("admission-create")

        # Tạo Admission
        admission = Admission.objects.create(
            pet=pet,
            room=room,
            admission_date=admission_date,
            discharge_date=discharge_date if discharge_date else None
        )

        # Tăng số lượng thú cưng trong phòng
        room.current_occupancy += 1
        room.update_status()
        room.save()

        return redirect("admission-list")

    pets = Pet.objects.all()
    rooms = Room.objects.filter(current_occupancy__lt=models.F('capacity'))
    return render(request, "app_admin/admission-create.html", {"pets": pets, "rooms": rooms})


# #Xuất viện và tạo hóa đơn

def admission_discharge(request, id):
    admission = get_object_or_404(Admission, id=id)

    # Cập nhật ngày xuất viện
    admission.discharge_date = now()
    admission.save()

    # Tạo hóa đơn thanh toán
   # Tạo hóa đơn nhưng chưa lưu
    invoice = Invoice(admission=admission, issued_date=now(), is_paid=False)

    # Tính tổng tiền trước khi lưu
    invoice.calculate_total()

    # Sau khi có total_amount, lưu invoice vào database
    invoice.save()
    

    # Giảm số lượng thú trong phòng
    room = admission.room
    if room.current_occupancy > 0:
        room.current_occupancy -= 1
    room.update_status()
    room.save()  # Cần lưu sau khi cập nhật trạng thái

    return redirect("invoice-detail", invoice.id)




def invoice_detail(request, id):
    invoice = get_object_or_404(Invoice, id=id)
    return render(request, "app_admin/invoice-detail.html", {"invoice": invoice})

def invoice_payment(request, id):
    invoice = get_object_or_404(Invoice, id=id)
    if request.method == "POST":
        invoice.is_paid = True
        invoice.payment_date = now()
        invoice.save()
        return redirect("admission-list")  # Quay lại danh sách nhập viện

    return render(request, "app_admin/invoice-payment.html", {"invoice": invoice})
