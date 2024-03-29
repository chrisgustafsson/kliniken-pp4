from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Booking
from .forms import BookingForm, UserLoginForm, CustomUserCreationForm


def index(request):
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


@login_required
def delete_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.delete()
    messages.success(request, 'Booking deleted successfully!')
    return redirect('my_bookings')


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('index')
            else:
                messages.error(request, 'Wrong username/password. Try again.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def signout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('index')


def error_view(request):
    return render(request, 'error.html')
