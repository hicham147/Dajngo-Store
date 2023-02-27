from .views import product_list,product_detail
from django.urls import path
app_name = 'App_stor'
urlpatterns = [
    path("", product_list,name="product_list"),
    path('<slug:category_slug>/', product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail,name='product_detail'),

]