from django.shortcuts import render
from django.http import HttpResponse
from django.urls.resolvers import re
def index(request):
    return HttpResponse("Welcome every morning with a smile. Look on the new day as another special gift from your Creator, another golden opportunity to complete what you were unable to finish yesterday. Be a self-starter. Let your first hour set the theme of success and positive action that is certain to echo through your entire day. Today will never happen again. Don't waste it with a false start or no start at all. You were not born to fail.")
