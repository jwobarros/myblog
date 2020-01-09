"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from blog.views import HomePageView, post_detail, subscribe_view


admin.site.site_header = 'Administração do site'
admin.site.index_title = 'Johnnatan Barros'
admin.site.site_title = 'Administração'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<slug:slug>/', post_detail, name='post-detail'),
    path('subscribe', subscribe_view, name='subscribe'),
    path(r'^favicon\.ico$', RedirectView.as_view(url='/staticfiles/favicon.ico')),
    path('admin/', admin.site.urls),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)