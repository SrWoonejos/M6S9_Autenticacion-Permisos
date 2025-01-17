from django.urls import path
from .views import input_book, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('inputbook/', input_book, name='input_book'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
