"""dianda URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from dianda import settings
from users.views import LoginView
from captcha.views import captcha_refresh
from django.conf.urls.i18n import i18n_patterns

from . import views

# 设置多语种
urlpatterns = [
    path('i18n/', i18n_patterns),
]

urlpatterns += [
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(), name='index'),  # 登录
    path('captcha', include('captcha.urls')),   # 生成验证码
    path('refresh/', captcha_refresh),          # 点击刷新验证码
    path('users/', include('users.urls')),      # 用户管理
    path('ocean/', include('ocean.urls')),      # 海运
    path('airfreight/', include('airfreight.urls')),  # 空运
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.server_error

