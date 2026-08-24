from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

def home(request):
    return HttpResponse("""
        <h1>Daily Tasks API</h1>
        <p>Welcome to the Daily Tasks Tracker backend!</p>
        <ul>
            <li><a href="/admin">Admin panel</a></li>
            <li><a href="/api/schema">API Schema</a></li>
        </ul>
    """)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]