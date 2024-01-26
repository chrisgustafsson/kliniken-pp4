from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking

# Create your views here.


def home(request):
    return render(request, "index.html")


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'mybookings.html', {'bookings': bookings})


@login_required
def edit_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        messages.success(request, 'Booking updated successfully!')
        return redirect('my_bookings')
    return render(request, 'editbooking.html', {'booking': booking})

