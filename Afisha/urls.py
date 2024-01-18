"""
URL configuration for Afisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from movie_app.views import director_view, director_detail_view, movie_view, movie_detail_view, review_view, \
    review_detail_view, review_movie_view, RegistrationAPIView, ConfirmUserAPIView, AuthorizationAPIView, \
    DirectoryListAPIView, DirectoryDetailAPIView, MovieListAPIView, MovieDetailAPIView, ReviewListAPIView, \
    ReviewDetailAPIView, ProductReviewListAPIView
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', director_view),
    path('api/v1/directors/<int:id>/', director_detail_view),
    path('api/v1/movies/', movie_view),
    path('api/v1/movies/<int:id>/', movie_detail_view),
    path('api/v1/reviews/', review_view),
    path('api/v1/reviews/<int:id>/', review_detail_view),
    path('api/v1/movies/reviews/', review_movie_view),
    # path('users/registration/', views.registration_api_view),
    # path('users/confirm/', views.confirm_user_api_view),
    # path('users/authorization/', views.authorization_api_view),
    path('users/registration/', RegistrationAPIView.as_view()),
    path('users/confirm/', ConfirmUserAPIView.as_view()),
    path('users/authorization/', AuthorizationAPIView.as_view()),
    path('products/categories/', DirectoryListAPIView.as_view()),
    path('products/categories/<int:pk>/', DirectoryDetailAPIView.as_view()),
    path('products/products/', MovieListAPIView.as_view()),
    path('products/products/<int:pk>/', MovieDetailAPIView.as_view()),
    path('products/reviews/', ReviewListAPIView.as_view()),
    path('products/reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('products/products/reviews/', ProductReviewListAPIView.as_view()),
]

