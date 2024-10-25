"""
URL configuration for warehouse_Django2 project.

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
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from .settings import *

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
    path('api/login/', login_user, name='login_user'),
    path('api/user/profile/', get_user_profile, name='user-profile'),
    path('api/barcode/',views.barcode_search),
    path('products_detail/<int:id>/',views.products_detail),
    
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'.*',views.error_page),
]