from django.conf.urls import url

from . import views

app_name = "dose"

urlpatterns = [
    url(r'^$', views.request_num, name='request_num'),
    url(r'^done$', views.done, name='done'),
]
