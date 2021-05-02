from django.shortcuts import render,redirect
from .forms import CaseForm
from django.views.generic import TemplateView, CreateView, DetailView, FormView
from .models import *
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from tablib import Dataset
from .resources import CaseResource
from .filters import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django import forms



# Create your views here.

def case_list(request):
    case_list = Case.objects.all()
    case_filter = CaseFilter(request.GET, queryset=case_list)
  #  status_filter = case_list.filter(status='Done').count()
    context = {'case':case_list,'filter':case_filter}
    return render(request,"case_register/case_list.html",context)

def case_form(request):
	form = CaseForm()
	if request.method == 'POST':
		form = CaseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/list')
	return render(request,"case_register/case_form.html",{'form': form})

'''def case_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = CaseForm()
        else:
            case = Case.objects.get(id=pk)
            form = CaseForm(instance=case)
        return render(request,"case_register/case_form.html",{'form': form})
    else :
        if id == 0:
            form = CaseForm(request.POST)
        else:
            case = Case.objects.get(id=pk)
            form =  CaseForm(request.POST,instance=case)
        if form.is_valid():
            form.save()
        return redirect('/list')'''
#def case_delete(request,id):

  #  case = Case.objects.get(pk=id)
   # case.delete()
   # return redirect('/list')
def case_update(request, pk):

	case = Case.objects.get(id=pk)
	form = CaseForm(instance=case)

	if request.method == 'POST':
		form = CaseForm(request.POST, instance=case)
		if form.is_valid():
			form.save()
			return redirect('/list')
	return render(request,"case_register/case_form.html",{'form': form})
class HomePage(TemplateView):
    template_name = "index.html"

   # def get(self, request, *args, **kwargs):
      #  if request.user.is_authenticated:
     #       return HttpResponseRedirect(reverse("test"))
      #  return super().get(request, *args, **kwargs)
