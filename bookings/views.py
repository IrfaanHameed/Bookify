from django.shortcuts import render, get_object_or_404
from .models import Flight, Booking
from .forms import BookingForm
import stripe
from django.conf import settings
from django.views.generic.base import View
from django.shortcuts import render, redirect



def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flight_list.html', {'flights': flights})

def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    return render(request, 'flight_detail.html', {'flight': flight})

def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.flight = flight
            booking.save()
            total_amount = booking.total_amount()
            return render(request, 'booking_confirmation.html', {'booking': booking, 'total_amount': total_amount})
    else:
        form = BookingForm()
    return render(request, 'book_flight.html', {'form': form, 'flight': flight})



