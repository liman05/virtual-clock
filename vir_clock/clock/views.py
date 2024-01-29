from django.shortcuts import render
from datetime import datetime


def view_clock(request):
    date= datetime.now()
    return render(request, 'clock.html', {'date': date})