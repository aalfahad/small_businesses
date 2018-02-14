# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Business
from .forms import BusinessForm
# Create your views here.


def business_list(request):
	context = {
		"objects": Business.objects.all(),
	}
	return render(request, 'business_list.html', context)

def business_detail(request, business_id):
	context = {
	"business": Business.objects.get(id=business_id),
	}
	return render(request,'business_detail.html',context)

def business_create(request):
	form = BusinessForm()
	if request.method == "POST":
		form = BusinessForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('business_list')
	context = {
		"create_form": form,
	}
	return render(request,'business_create',context)

def business_update(request,business_id):
	business_obj= Business.objects.get(id=business_id)
	form = BusinessForm(instance = business_id)
	if request.method == "POST":
		form = BusinessForm(request.POST,instance= business_obj)
		if form.is_valid():
			form.save()
			return redirect("business_detail", business_id=business_obj.id)
	context = {
		"business_obj": business_obj,
		"create_form": form, 
	}
	return render(request,'business_update.html',context)

def delete(request, business_id):
	Business.objects.get(id=business_id).delete()
	return redirect("business_list")







