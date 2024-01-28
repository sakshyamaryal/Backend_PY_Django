from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'playground'

urlpatterns = [
    path('', TemplateView.as_view(template_name = "blog/index.html")),
    # path('hello/', views.say_hello)
]
