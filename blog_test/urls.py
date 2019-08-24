"""blog_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.conf import settings

from booksdata.views import books
from login import views
from django.conf.urls import url, include, static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^booksdata/', include('booksdata.urls')),
    url(r'^userlogin/', include('login.urls')),
    url(r'^captcha', include('captcha.urls')),
    url(r'^userlogin/login/', views.login),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^upload-image', books.upload_image, name='upload_image'),
    # url(r'^ckeditor/', include('ckeditor.urls')),
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)