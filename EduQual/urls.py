from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('users.urls')),
    path('accounts/', include('users.urls')),
    path('', include('poll.urls')),
]
