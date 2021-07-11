from django.contrib import admin
from django.urls import path, include
from Product import urls as Product_urls
urlpatterns = [
    path('pd_lists/',include(Product_urls)), #  everything that starts with app2 urls， to app2 (app the name ) the urls. py to deal with 
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('Product.urls')),
    
]