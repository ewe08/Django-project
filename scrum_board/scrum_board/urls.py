from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls'), name='homepage'),
    path('feedback/', include('feedback.urls'), name='feedback'),
    path('admin/', admin.site.urls),
]
