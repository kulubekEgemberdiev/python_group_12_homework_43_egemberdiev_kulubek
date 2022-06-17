from django.urls import path

from webapp.views import index_view, first_view, second_view, third_view

urlpatterns = [
    path('', index_view),
    path('first/', first_view),
    path('second/', second_view),
    path('third/', third_view)
]