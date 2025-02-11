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
    try:
        room = Room.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse("Room not found", status=404)

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

#Tạo mới một ca nhập viện
# def admission_create(request):
#     if request.method == "POST":
#         pet_id = request.POST.get("pet")
#         room_id = request.POST.get("room")

#         pet = get_object_or_404(Pet, id=pet_id)
#         room = get_object_or_404(Room, id=room_id)

#         # Tạo Admission
#         admission = Admission.objects.create(pet=pet, room=room, admission_date=now())

#         # Cập nhật trạng thái phòng
#         room.status = "Occupied"
#         room.save()

#         return redirect("admission-list")

#     pets = Pet.objects.all()
#     rooms = Room.objects.filter(status="Available")  # Chỉ hiển thị phòng trống
#     return render(request, "app_admin/admission-create.html", {"pets": pets, "rooms": rooms})

from django.db import models  # Import đúng models.F

def admission_create(request):
    if request.method == "POST":
        pet_id = request.POST.get("pet")
        room_id = request.POST.get("room")

        pet = get_object_or_404(Pet, id=pet_id)
        room = get_object_or_404(Room, id=room_id)

        # Kiểm tra nếu phòng đã đầy
        if room.current_occupancy >= room.capacity:
            return HttpResponse("Room is already full!", status=400)

        # Tạo Admission
        admission = Admission.objects.create(pet=pet, room=room, admission_date=now())

        # Tăng số lượng thú cưng trong phòng
        room.current_occupancy += 1
        room.update_status()
        room.save()  # Cần lưu sau khi cập nhật trạng thái

        return redirect("admission-list")

    pets = Pet.objects.all()
    rooms = Room.objects.filter(current_occupancy__lt=models.F('capacity'))  # Chỉ hiển thị phòng chưa đầy
    return render(request, "app_admin/admission-create.html", {"pets": pets, "rooms": rooms})



# #Xuất viện và tạo hóa đơn
# def admission_discharge(request, id):
#     admission = get_object_or_404(Admission, id=id)
    
#     # Cập nhật ngày xuất viện
#     admission.discharge_date = now()
#     admission.save()

#     # Tạo hóa đơn thanh toán
#    # Tạo hóa đơn nhưng chưa lưu
#     invoice = Invoice(admission=admission, issued_date=now(), is_paid=False)

#     # Tính tổng tiền trước khi lưu
#     invoice.calculate_total()

#     # Sau khi có total_amount, lưu invoice vào database
#     invoice.save()
    
#     # Giải phóng phòng
#     admission.room.status = "Available"
#     admission.room.save()

#     # Cập nhật lại admission để có thông tin invoice
#     admission.refresh_from_db()

#     return redirect("invoice-detail", invoice.id)

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
