from django.urls import path, include

from photos import views

urlpatterns = [
    path = ('latest-products/', views.LastestProductsList.as_view()),
]