from django.urls import path, include

from .views import Product


urlpatterns = [
    path('lastest-products/', views.LatestProductsList.as_view()),

]
