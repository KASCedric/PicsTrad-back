from django.conf.urls import url

from picstrad import views

urlpatterns = [
    url(r'^$', views.my_view, name="my_view"),
    url(r'^cedric$', views.ced, name="ced"),
    url(r'^weight$', views.year_of_birth, name="year_of_birth"),
    url(r'^image$', views.image, name="image"),
]
