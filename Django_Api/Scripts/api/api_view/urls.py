from django.contrib import admin
from django.urls import path
from api_view.views import product_list, product_create, action


urlpatterns = [
    path('list/', product_list),
    path('add/', product_create),
    path('<int:pk>', action)
]
