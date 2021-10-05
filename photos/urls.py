from django.urls import path, include

from photos import views


urlpatterns = [
    path('lastest-products/', views.LatestProductsList.as_view()),

]
