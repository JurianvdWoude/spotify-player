
from django.urls import path, include
from .views import AuthURL, IsAuthenticated, spotify_callback

urlpatterns = [
    path('get-auth-url', AuthURL.as_view()),
    path('is-authenticated', IsAuthenticated.as_view()),
    path('redirect', spotify_callback)
]