from django.urls import path
from .views import app1_view, app1_second_view

urlpatterns = [
    path('', app1_view, name='app1_view'),  # URL for app1 view
	path('second/', app1_second_view, name='app1_second_view'),  # URL for second view in app1
]
