from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls')),
    path('tasks/', include('board.urls')),
    path('admin/', admin.site.urls),
]
