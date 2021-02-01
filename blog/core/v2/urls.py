from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>', views.begin, name='get_name'),
    path('register/<str:name>', views.write,  name='register'),
]
