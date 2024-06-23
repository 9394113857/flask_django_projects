from django.urls import path
from .views import app2_view, app2_second_view

urlpatterns = [
    path('', app2_view, name='app2_view'),  # URL for app2 view
	path('2/', app2_second_view, name='app2_second_view'),  # URL for second view in app2
]
