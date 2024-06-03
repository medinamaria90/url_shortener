from datetime import date
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.utils import timezone
from api.models import Shorterlink

from django.shortcuts import render

def url_redirection(request, short_link):
    today = date.today()
    short_link_obj = get_object_or_404(Shorterlink, short_link=short_link)
    short_link_obj.clicks += 1
    short_link_obj.last_click = today 
    short_link_obj.save()    
    if short_link_obj.expiration < today:
        return HttpResponse("This link has expired.", status=410)  # 410 Gone
    return HttpResponseRedirect(short_link_obj.link)