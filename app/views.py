from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from app.models import *


class Home(TemplateView):
    template_name = 'app/home.html'
    
    
class SchoolList(ListView):
    model = School
    context_object_name = 'schools'
    
    
class SchoolDetail(DetailView):
    model = School
    context_object_name = 'sclobject'
    
class SchoolCreate(CreateView):
    model = School
    fields = '__all__'
    
    
class SchoolUpdate(UpdateView):
    model = School
    fields = '__all__'
    
class SchoolDelete(DeleteView):
    model = School
    context_object_name = 'schoolobject'
    success_url = reverse_lazy('SchoolList')
    
class StudentCreate(CreateView):
    model = Student
    fields='__all__'
    success_url = reverse_lazy('SchoolList')
    
class StudentDetail(DetailView):
    model = Student
    context_object_name = 'stuobject'
    
class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'