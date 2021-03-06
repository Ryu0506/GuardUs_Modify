from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('posting/',include('posting.urls')),
    path('accounts/', include('accounts.urls')),
    re_path(r'^accounts/', include('allauth.urls')),
    path('', include('posting.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)