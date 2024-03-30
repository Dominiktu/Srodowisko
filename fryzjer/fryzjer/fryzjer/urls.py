from django.contrib import admin
from django.urls import path,include
from ap import views 

urlpatterns = [
    path('', include("ap.urls")),
    path('admin/', admin.site.urls),
]