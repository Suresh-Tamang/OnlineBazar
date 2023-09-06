from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,'AppOnlineBazar/index.html')


def Register(request):
    return render(request,'AppOnlineBazar/register.html')

def Login(request):
    return render(request,'AppOnlineBazar/login.html')

