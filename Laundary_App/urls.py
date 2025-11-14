from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('service/', views.service, name='service'),
    path('pricing/', views.pricing, name='pricing'),
    path('logout/', views.logout, name='logout'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
]
