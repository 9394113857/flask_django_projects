from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_view(request):
	return HttpResponse("This is a view for app1!")
	
def app1_second_view(request):
    return HttpResponse("This is the second view for app1!")	