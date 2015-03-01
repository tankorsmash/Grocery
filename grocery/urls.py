from django.conf.urls import patterns, include, url
from django.contrib import admin


from django.http import HttpResponse

from django.shortcuts import render_to_response

from models import FoodItem, Aisle, Store, Company

def index(request):
    context = {
            "companies" : Company.objects.all(),
            }
    return render_to_response("grocery/index.html", context)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'grocery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
)
