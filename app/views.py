from django.shortcuts import render
from app.models import *
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.

class Home(TemplateView):
    template_name='app/Home.html'

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

class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobj'
    success_url=reverse_lazy('Schoollist')

