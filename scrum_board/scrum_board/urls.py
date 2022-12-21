from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls')),
    path('users/', include('users.urls')),
    path('board/', include('board.urls')),
    path('admin/', admin.site.urls),
]
