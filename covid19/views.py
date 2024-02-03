from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")
def loginpage(request):
    return render(request, "login.html")