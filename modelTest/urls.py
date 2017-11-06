from django.conf.urls import url
from .views import show_mes,filterTest

urlpatterns = [
    url(r'^show',show_mes),
	url(r'^filter',filterTest),
]