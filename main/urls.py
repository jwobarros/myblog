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
    path('favicon.ico', RedirectView.as_view(url='/staticfiles/favicon.ico')),
    path('admin/', admin.site.urls),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)