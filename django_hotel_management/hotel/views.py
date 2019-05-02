from django.shortcuts import render
from django.http import HttpResponse
from .models import Reservation
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    context = {
        'reservations': Reservation.objects.all()
    }
    return render(request, 'hotel/home.html',context)
@login_required
def about(request):
    return render(request, 'hotel/about.html',{'title': 'New About'})
