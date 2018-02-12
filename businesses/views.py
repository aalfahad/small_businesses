# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Business
# Create your views here.
def home(request):
	context = {
		"businesses": Business.objects.all(),
	}
	return render(request, "home.html", context)

def home_detail(request, businesses_id):
	instance = Business.objects.get(id=businesses_id)
	context = {
	"title": "Detail",
	"instance": instance,
	}
	return render(request,'home_detail.html',context)