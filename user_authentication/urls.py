from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile_home/', views.profile_home, name = 'profile_home'),
    path('profile_settings/', views.profile_settings, name = 'profile_settings'),
    path('signup/', views.signup, name = 'signup'),
    path('', auth_views.LoginView.as_view(template_name = 'login.html'),
         name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'),
    path('delete_city/<city_id>/', views.delete_city, name = 'delete_city'),
    path('set_hometown/<hometown_id>', views.set_hometown, name = 'set_hometown'),
]