from django.contrib import admin
from django.urls import path
from api_view.views import  product_list, product_create, action, product_category_list, product_category_create, product_category_action ,promotion_action ,promotion_create, promotion_list


urlpatterns = [
    path('plist/', product_list),
    path('clist/', product_category_list),
    path('prlist/', promotion_list),
    path('padd/', product_create),
    path('cadd/', product_category_create),
    path('pradd/', promotion_create),
    path('<int:pk>', action),
    path('id=<int:pk>', product_category_action),
    path('prid=<int:pk>', promotion_action)
]
