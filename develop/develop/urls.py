from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('template/', include('playground.urls', namespace='playground')),
    path('api/', include('dev_api.urls', namespace='dev_api')),
    # path('playground/', include('playground.urls')),
]
