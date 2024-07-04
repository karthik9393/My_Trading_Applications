from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('trading.urls')),  # Make sure to include the app's URLs
]
