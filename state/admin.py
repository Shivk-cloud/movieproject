from django.contrib import admin
from .models import Movie, Customer


class MovieAdmin(admin.ModelAdmin):
    list_display =['title','length','release_year']

class customerAdmin(admin.ModelAdmin):
    list_display =['first_name', 'last_name', 'phone']
    list_editable = ['phone']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Customer, customerAdmin)
