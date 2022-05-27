from django.shortcuts import render



def index(request):
    return render(request,'home.html')


def mapview(request):
    return render(request,'map.html')
