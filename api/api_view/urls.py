from django.contrib import admin
from django.urls import path
from api_view.views import  product_list, product_create, action, product_category_list, product_category_create, product_category_action


urlpatterns = [
    path('plist/', product_list),
    path('clist/', product_category_list),
    path('padd/', product_create),
    path('cadd/', product_category_create),
    path('<int:pk>', action),
    path('id=<int:pk>', product_category_action)
]
