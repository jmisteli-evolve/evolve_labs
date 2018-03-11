from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('blob', views.blob, name='blob')
]