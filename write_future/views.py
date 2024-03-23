from django.shortcuts import render
from datetime import datetime


def index(request):
    message = "Hello World!"
    return render(request, 'index.html',
                  {'hello': message, "datetime": datetime.now()})