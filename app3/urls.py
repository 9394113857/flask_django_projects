from django.urls import path
#from app3.views import addition, multiplication, subtraction, division

from . import views

app_name = 'app3'

'''
urlpatterns = [
    path('addition/<int:num1>/<int:num2>/', addition, name='addition'),
    path('multiplication/<int:num1>/<int:num2>/', multiplication, name='multiplication'),
	path('subtraction/<int:num1>/<int:num2>/', subtraction, name='subtraction'),
	path('division/<int:num1>/<int:num2>/', division, name='division'),	
]
'''

urlpatterns = [
    path('<str:operation>/<int:num1>/<int:num2>/', views.calculate, name='calculate'),
]

# 	path('<str:operation>/<int:num1>/<int:num2>/', views.calculate, name='calculate'),
