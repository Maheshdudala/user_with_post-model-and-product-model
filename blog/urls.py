from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
     path('admin/', admin.site.urls),
    
    path('',views.home,name="home"),
    path('reg',views.add_user,name="adduser"),
    path('login',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),

    path('post_lists', views.post_list, name='post_lists'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit1/', views.post_edit, name='post_edit'),

]