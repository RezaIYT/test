from django.urls import path
from django.contrib import admin
from api.views import calculate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate/', calculate.as_view(), name='calculate'),
]
