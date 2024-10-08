"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from myapp.views import *
from myapp import views
from django.contrib.auth import views as auth_views
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login_view, name='login'),
    path('captcha/', include('captcha.urls')),
    path('', views.home_view, name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('products/', views.product_list, name='product_list'),
    path('products/update/<int:product_id>/', views.update_quantity, name='update_quantity'),
    path('products/add/', views.add_product, name='add_product'),  # 新增貨品的 URL
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),  # 刪除貨品的 URL
    path('signup/', views.signup, name='signup'),  # 註冊頁面
    path('api/products/', ProductListAPIView.as_view(), name='product_list_api'),  # 所有貨品列表
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail_api'),  # 單一貨品
    path('api/users/', UserListAPIView.as_view(), name='user_list_api'),  # 所有使用者
    path('api/users/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail_api'),  # 單一使用者
    path('api/login/', login_user, name='login_user'),
    path('api/user/profile/', get_user_profile, name='user-profile'),
    
    re_path(r'.*/',views.error_page),
]
