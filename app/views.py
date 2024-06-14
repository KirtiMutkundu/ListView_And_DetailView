from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView
from django.http import HttpResponse

# Create your views here.

class Schoollist(ListView):
    model=School
    context_object_name='schools'
    #queryset=School.objects.filter(sname='Qspiders')
    #ordering=['sname']

def wish(request,n):
    return HttpResponse(f'Hai {n} How Are You') #In browser runserver with wish/Kirti or wish/arg bz wish takes 2args

#In browser search with *Schoollist* and click on Hyperlink, keep changing primary key value 1/2/3. 
#DONOT search with SchoolDetail.
class SchoolDetail(DetailView): 
    model=School
    context_object_name='schoolobject'
