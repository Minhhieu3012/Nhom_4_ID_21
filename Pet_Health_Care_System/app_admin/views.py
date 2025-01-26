from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from app_admin.models import Room

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

def room_edit(request):
    room = Room.objects.get(id = 1)
    template = loader.get_template('app_admin/room-edit.html')
    context = {
        'room' : room, 
    }
    return HttpResponse(template.render(context, request))