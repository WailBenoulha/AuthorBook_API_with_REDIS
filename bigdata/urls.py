# urls.py (inside your project directory)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Adjust the app name accordingly
    # Add other URL patterns as needed
]
