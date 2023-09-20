from django.urls import path
from .views import indexTemplateView

urlpatterns = [
    path('', indexTemplateView.as_view()),
]
