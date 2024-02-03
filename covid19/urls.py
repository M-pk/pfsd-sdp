from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage,name=""),
    path('login', views.loginpage, name="login"),
    path('',include('adminapp.urls')),

]