from django.conf.urls import url
from djangoTemplate import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^data/$', views.DataPageView.as_view(), name='data'),
]
