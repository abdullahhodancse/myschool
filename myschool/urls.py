from django.contrib import admin
from django.urls import path, include  # import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),  # correct syntax for including app URLs
]
