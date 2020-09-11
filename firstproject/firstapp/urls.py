from django.conf.urls import url
from firstapp import views


urlpatterns = [
    url(r'', views.Help, name='Help')
]