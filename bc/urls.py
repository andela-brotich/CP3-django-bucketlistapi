from django.conf.urls import url

from bc.api import views

urlpatterns = [
    url(r'^$', views.index, name="bc-index")
]
