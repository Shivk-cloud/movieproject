from django.shortcuts import render
# Create your views here.

def base(request):
    # data=Movie.objects.all()
    # print(data)
    return render(request,"base.html",{})