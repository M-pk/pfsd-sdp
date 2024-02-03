
from.import views
from os import path
from django.urls import path
urlpatterns=[
    path("home",views.home,name="home"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
]