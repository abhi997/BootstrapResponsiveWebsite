
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from profiles import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Home, name='home'),
    url(r'^about/', views.About, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
