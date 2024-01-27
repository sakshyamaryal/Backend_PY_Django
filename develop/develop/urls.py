from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('playground.urls', namespace='playground')),
    # path('api', include('playground_api.urls', namespace='playground_api')),
    # path('playground/', include('playground.urls')),
]
