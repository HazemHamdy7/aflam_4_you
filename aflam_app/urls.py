from django.urls import path
from .import views


urlpatterns = [
    path('', views.Home, name='Home'),
    # path('login', views.login, name='login'),
    # path('signup', views.signup, name='signup'),
    # path('logout', views.logout, name='logout'),

]
