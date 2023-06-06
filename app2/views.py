from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_view(request):
    return HttpResponse("This is a view for app2!")
	
def app2_second_view(request):
    return HttpResponse("This is the second view for app2!")	