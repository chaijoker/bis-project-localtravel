from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Booking, User, Trip


def create(request,id):
    if request.method == 'POST':
        if request.method == "POST":
            user = request.user
            trip = get_object_or_404(Trip,id=id)
            image_pay = request.FILES.get('img_photo',None)

            booking = Booking.objects.create(user=user, trip=trip, image_pay=image_pay
                                           )
            booking.save()


            trip.booking_status = False

            trip.save()

        return render(request, 'travel/index.html',)

    return render(request, 'travel/trip.html',)
