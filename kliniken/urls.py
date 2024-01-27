from django.urls import path
from .views import index, my_bookings, edit_booking, delete_booking, login_view, signup_view, signout_view, error_view

urlpatterns = [
    path("", index, name="index"),
    path('mybookings/', my_bookings, name='my_bookings'),
    path('editbooking/<int:booking_id>/', edit_booking, name='edit_booking'),
    path('deletebooking/<int:booking_id>/',
         delete_booking, name='delete_booking'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('signout/', signout_view, name='signout'),
    path('error/', error_view, name='error'),
]
