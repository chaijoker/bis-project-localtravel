from django.contrib import admin
from .models import Trip, Guide, Booking
# Register your models here.
class trip_display(admin.ModelAdmin):
    list_display = ('id','title','place','price_trip','type_price','phone','date','time_start','time_end','booking_status')
admin.site.register(Trip,trip_display)


class guide_display(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','username','email','telephone','nationalID')
admin.site.register(Guide,guide_display)


class booking_display(admin.ModelAdmin):
    list_display = ('id','user','trip','image_pay')
admin.site.register(Booking,booking_display)