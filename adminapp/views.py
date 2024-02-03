from django.shortcuts import render
from .models import Admin
def home(request):
    return render(request,"home.html")

def loginfail(request):
    return render(request,"loginfail.html")

# we need to define the urls mapping for this 2 functions defined at views.py.
def checkadminlogin(request):
    if request.method == "POST":
        adminuname = request.POST["uname"]
        adminpwd = request.POST["password"]
        flag = Admin.objects.filter(username=adminuname,password=adminpwd).values()
        if flag:
            return render(request,"home.html")
        else:
         return render(request,"loginfail.html")




