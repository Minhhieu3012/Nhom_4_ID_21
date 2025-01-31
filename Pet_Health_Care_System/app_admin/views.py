from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from app_admin.models import Room
from django.core.exceptions import ObjectDoesNotExist



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
    rooms = Room.objects.all()
    template = loader.get_template('app_admin/rooms.html')
    context = {
        'room' : rooms, 
    }
    return HttpResponse(template.render(context, request))

# def room_edit(request):
#     room = Room.objects.get(id = 3)
#     template = loader.get_template('app_admin/room-edit.html')
#     context = {
#         'room' : room, 
#     }
#     return HttpResponse(template.render(context, request))


# def room_edit(request):
#     try:
#         # Cố gắng lấy room từ database
#         room = Room.objects.get(id=1)
#     except ObjectDoesNotExist:
#         # Nếu room không tồn tại, cung cấp dữ liệu mặc định
#         room = {
#             'room_type': 'Standard',  # Giá trị mặc định
#             'capacity': 0,           # Số lượng mặc định
#             'status': 'Available',   # Trạng thái mặc định
#         }

#     template = loader.get_template('app_admin/room-edit.html')
#     context = {
#         'room': room, 
#     }
#     return HttpResponse(template.render(context, request))

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
def room_delete(request, id):
    # Lấy phòng từ database, nếu không tìm thấy thì trả về lỗi 404
    room = get_object_or_404(Room, id=id)

    # Xóa phòng
    room.delete()

    # Chuyển hướng về trang danh sách phòng sau khi xóa
    return redirect('rooms')
