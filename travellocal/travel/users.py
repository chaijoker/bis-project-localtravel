from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

def edit(request, username):
    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user = User.objects.filter(username=username).first()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

    return redirect('/dashboard')

def delete(request, username):
    user = User.objects.filter(username=username).first()
    user.delete()
    print(user.username)

    return redirect('/dashboard')

