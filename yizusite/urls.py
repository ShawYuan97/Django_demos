"""yizusite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from captcha.views import captcha_refresh
from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index_view),
    path('login/', views.login_view),
    path('register/', views.register_view),
    path('logout/', views.logout_view),
    # 图形验证码功能
    path('captcha/', include('captcha.urls')),
    path('refresh/', captcha_refresh),
    # 处理注册邮件请求
    path('confirm/', views.user_confirm_view),

    # 事务子路由
    path('affair/', include('affair.urls')),

    # 仿真系统子路由
    path('neuromorphic/', include('neuromorphic.urls')),

    # 子路由

]
