from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Movie
from django.views import View
from .forms import Movieform
# Create your views here.

class index(View): # Note: Using View instead of view
  def get(self, request):
    data=Movie.objects.all()
    return render(request, 'basee.html',{'data':data})


# def Add(request):
#     fm=Movieform()
#     if request.method=="POST":
#         fm=Movieform(request.POST)
#         if fm.is_valid():
#             fm.save()
#             return redirect('index/')
#     template_name = 'add.html'
#     context = {'fm': fm}
#     return render(request, template_name, context)


def Add(request):
    if request.method == 'POST':
        fm = Movieform(request.POST)
        if fm.is_valid():
            fm.save()
            # Redirect or perform some action after saving
    else:
        fm = Movieform()
    return render(request, 'add.html', {'fm': fm})
    
