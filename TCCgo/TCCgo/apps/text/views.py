import json
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
from pprint import pprint

from .controller import (
    TextController
)
from .models import (
    Text, Fragment
)

def index(request):
    return render(request, 'index.html');

# Create your views here.
def text_page(request):
	return render(request, 'submit.html')

def all_texts_page(request):
	return render(request, 'list.html')

def create_text(request):
    """ create a new text """
    status = TextController().request_create(request)
    if status == 200:
        return JsonResponse({'success':True, 'url':'127.0.0.1:8000'}, safe=False)
    else:
        return JsonResponse({'success':False}, safe=False)

def delete_text(request):
    """ Delete text from request"""
    status = TextController().request_delete(request)
    if status == 200:
        return JsonResponse({'success':True, 'url':'127.0.0.1:8000'}, safe=False)
    else:
        return JsonResponse({'success':False}, safe=False)

def get_all_texts(request):
    """ Return all texts"""
    query_set = TextController.get_all(request.user)
    data = serializers.serialize('json', query_set)
    return JsonResponse(data, safe=False)

def filter_texts(request):
    """ Return a filtered by name set of texts"""
    query_set = TextController().request_filter(request)
    response =  serializers.serialize('json', query_set)
    return JsonResponse(response, safe=False)
