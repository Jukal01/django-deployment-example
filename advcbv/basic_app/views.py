from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'basic_app/index.html' 



class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'basic_app/school_list.html'



class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/detail.html'

class SchoolCreateView(CreateView):
    model = models.School
    template_name = 'basic_app/school_form.html'
    fields = ('name','principal','location')

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name','principal')

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:schools')




     
