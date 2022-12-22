from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls'), name='homepage'),
    path('feedback/', include('feedback.urls'), name='feedback'),
    path('boards/', include('board.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
