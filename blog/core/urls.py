from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('to_be/<str:name>', views.BeginView.as_view(), name='get_name'),
    path('register', views.RegisterView.as_view(),  name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
]
