from django.shortcuts import render
from datetime import datetime


def index(request):
    message = "Hello World!"
    print(request.META)
    return render(request, 'index.html',
                  {'hello': message, "datetime": datetime.now()})