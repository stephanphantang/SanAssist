from django.urls import path

from . import views

urlpatterns = [
        path('show_result', views.show_result)
        # path('', views.index)
        ]

