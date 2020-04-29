from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Trip

def index(request):
    if request.method == 'POST':
        pass
    trips = Trip.objects.filter()
    return render(request, 'travel/posttrip.html',)

def create(request):
    if request.method == 'POST':
        if request.method == "POST":
            title = request.POST['title']
            place = request.POST['place']
            detail_place = request.POST['detail_place']
            detail_trip = request.POST['detail_trip']
            price_trip = request.POST['price_trip']
            type_price = request.POST['type_price']
            phone = request.POST['phone']
            date = request.POST['date']
            time_start = request.POST['time_start']
            time_end = request.POST['time_end']
            photo = request.FILES.get('img_photo',None)
            user = request.user

            trip = Trip.objects.create(title=title, place=place, detail_trip=detail_trip, detail_place=detail_place,
                                       price_trip=price_trip, type_price=type_price, phone=phone, date=date,
                                       time_start=time_start, time_end=time_end, image_trip=photo,
                                       user=user)
            trip.save()
            return render(request, 'travel/index.html',)

    return render(request, 'travel/posttrip.html',)

def update(request, id):
    if request.method == 'POST':
        trip = get_object_or_404(Trip,id=id)
        trip.title = request.POST['title']
        trip.place = request.POST['place']
        trip.phone = request.POST['phone']
        trip.date = request.POST['date']
        trip.time_start = request.POST['time_start']
        trip.time_end = request.POST['time_end']
        trip.save()
        print('post')

    return redirect('/dashboard')

def delete(request, id):
    trip = Trip.objects.filter(id=id)
    trip.delete()

    return redirect('/dashboard')