from django.conf.urls import url
from . import views

urlpatterns = [

    #url(r'^products/$', views.product_list), #used when method based view <check views.py>
    url(r'^products/$', views.ProductList.as_view()), #used when class based view <check views.py>
]
