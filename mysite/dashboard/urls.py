from django.urls import path
from .views import (home_page, shop_list, shop_create, shop_edit, shop_delete,
                    category_list, category_create, category_edit, category_delete,
                    product_list, product_create, product_edit, product_delete, login_page, logout_page)


urlpatterns = [
    path('', home_page, name='home_page'),
    path("login/", login_page, name='login_page'),
    path("logout/", logout_page, name='logout_page'),

    path('shop/list/', shop_list, name='shop_list'),
    path('shop/create/', shop_create, name='shop_create'),
    path('shop/<int:pk>/edit/', shop_edit, name='shop_edit'),
    path('shop/<int:pk>/delete/', shop_delete, name='shop_delete'),

    path('category/list/', category_list, name='category_list'),
    path('category/create/', category_create, name='category_create'),
    path('category/<int:pk>/edit', category_edit, name='category_edit'),
    path('category/<int:pk>/delete', category_delete, name='category_delete'),


    path('product/list/', product_list, name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/<int:pk>/edit', product_edit, name='product_edit'),
    path('product/<int:pk>/delete', product_delete, name='product_delete'),
]

####cool
###12345

