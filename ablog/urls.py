from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('blogapp.urls')),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
    # API part
    path('post-api/', include('blogapi.urls')),
    path('accounts/', include('allauth.urls')),

    path('social-auth/', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
