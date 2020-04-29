from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Trip, Guide, Booking
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.models import User, auth


def Home(request):
    trip = Trip.objects.all()
    context = {
        'trip':trip,
    }

    return render(request, 'travel/index.html',context)

def Dashboard(request,id):
    user_u = User.objects.all().filter(is_staff = False)
    user_g = User.objects.all().filter(is_staff = True , is_superuser = False)
    user_a = User.objects.all().filter(is_superuser = True)
    users = User.objects.all()
    trip = Trip.objects.all()
    trip_g = Trip.objects.all().filter(user=id)
    booking = Booking.objects.all()
    context = {
        'user_u':user_u,
        'user_g':user_g,
        'user_a':user_a,
        'users': users,
        'trip':trip,
        'trip_g':trip_g,
        'booking':booking
    }
    return render(request, 'travel/admin.html',context)

def Trips(request):
    trip = Trip.objects.all()

    paginator = Paginator(trip, 6)

    page = request.GET.get('page')

    trip = paginator.get_page(page)

    count = paginator.count

    context = {
        'count': count,
        'trip':trip,
        'paginator' : paginator
    }
    return render(request, 'travel/trip.html',context)

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("../")
        else:
            messages.info(request,'invalid credentials')
            return render(request,'travel/login.html')

    else:
        return render(request, 'travel/login.html')

def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('../register')
            elif User.objects.filter(email= email).exists():
                messages.info(request, 'Email Taken')
                return redirect('../register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('../login')

        else:
            print('Password not macthing..')
            return redirect('../register')

    else:
        return render(request, 'travel/register.html')

def Dtrip(request,id):
    trip = Trip.objects.filter(id=id)
    context = {
        'trip':trip
    }
    return render(request, 'travel/dtrip.html',context)



def Profile(request,id):
    users = User.objects.all()
    booking = Booking.objects.all().filter(user=id)
    context = {
        'users': users,
        'booking': booking
    }
    return render(request, 'travel/profile.html',context
                  )

def Posttrip(request):
    if request.method == "POST":
        title = request.post['title']
        place = request.post['place']
        detail_place = request.post['detail_place']
        detail_trip = request.post['detail_trip']
        phone = request.post['phone']
        date = request.post['date']
        time_start = request.post['time_start']
        time_end = request.post['time_end']
        photo = request.FILES['photo']
        user = request.user

        trip = Trip.objects.create(title=title,place=place,detail_trip=detail_trip,detail_place=detail_place,phone=phone,date=date,time_start=time_start,time_end=time_end,photo=photo,user=user)
        trip.save()
        return redirect('travel/posttrip.html')

    else:
        return render(request, 'travel/posttrip.html',)

def Registerguide(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('../registerguide')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('../registerguide')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name,username=username,
                                                 password=password1, email=email, is_staff=True
                                                )
                user.save();
                print('user created')
                return redirect('../login')

        else:
            print('Password not macthing..')
            return redirect('../registerguide')

    else:
        return render(request, 'travel/registerguide.html')


