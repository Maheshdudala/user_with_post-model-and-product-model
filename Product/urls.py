from blog.views import home
from django.urls import path
from Product import views as v

urlpatterns = [

    
    path('pd_list/',v.pd_list),
    path('post/<int:pk>/d/', v.pd1_detail, name='pd1_detail'),
    path('post/new1/', v.pd1_new, name='pd1_new'),
    path('post/<int:pk>/edit/s/', v.pd1_edit, name='pd1_edit'),
]