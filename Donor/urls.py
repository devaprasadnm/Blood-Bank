from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add-donor',views.form,name='form'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('display',views.display,name='display'),
]
