from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blogapp.urls')),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
]
