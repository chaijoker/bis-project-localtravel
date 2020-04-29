#travel/urls.py

from django.urls import path
from .views import Home, Trips, Login, Register, Dtrip, Dashboard, Profile, Posttrip, Registerguide

from . import users
from . import trips
from . import bookings

urlpatterns = [
    path('', Home,name='index-page'),
    path('trip/', Trips,name='trip-page'),
    path('login/', Login,name='login-page'),
    path('dtrip/<int:id>',Dtrip,name='dtrip-page'),
    path('register/', Register,name='register-page'),
    path('registerguide/', Registerguide,name='registerguide-page'),
    path('dashboard/<int:id>', Dashboard,name='dashboard-page'),
    path('profile/<int:id>', Profile,name='profile-page'),
    path('posttrip/', Posttrip,name='posttrip-page'),
    path('users/<username>', users.edit, name='users-edit'),
    path('users/delete/<username>', users.delete, name='users-delete'),
    path('trips', trips.index, name='trips-index'),
    path('trips/create', trips.create, name='trips-create'),
    path('trips/update/<int:id>', trips.update, name='trips-update'),
    path('trips/delete/<int:id>', trips.delete, name='trips-delete'),
    path('bookings/create/<int:id>', bookings.create, name='booking-create')
]