from django.urls import path

from .views import ListPageView

urlpatterns = [
    path('', ListPageView.as_view(), name='posts')
]
