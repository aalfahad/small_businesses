"""small_businesses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from businesses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('random/', views.home,name = "home"),
    #path('detail/<int:businesses_id>/',views.home_detail,name="home_detail"),
    path('business_list',views.business_list,name="business_list"),
    path('business_detail/<int:business_id>/',views.business_detail,name="business_detail"),
    path('create/',views.business_create,name="business_create"),
    path('update/<int:business_id>/',views.business_update,name="business_update"),
    path('delete/<int:business_id>/',views.delete,name="delete")
]
