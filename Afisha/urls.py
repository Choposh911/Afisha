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
    review_detail_view, review_movie_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', director_view),
    path('api/v1/directors/<int:id>/', director_detail_view),
    path('api/v1/movies/', movie_view),
    path('api/v1/movies/<int:id>/', movie_detail_view),
    path('api/v1/reviews/', review_view),
    path('api/v1/reviews/<int:id>/', review_detail_view),
    path('api/v1/movies/reviews/', review_movie_view),
]
