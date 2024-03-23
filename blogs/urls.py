from django.urls import path

from blogs.api.api_v1 import api as api_v1
from blogs.api.api_v2 import api as api_v2

app_name = 'blogs'
urlpatterns = [
    path("api/v1/", api_v1.urls),
    path("api/v2/", api_v2.urls),
]
