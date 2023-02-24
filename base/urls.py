from django.urls import path
from .views import ArtistList, WorkList , register
# RegistrationAPIView


urlpatterns = [
    # path('clients/', ClientList.as_view(), name='client-list'),
    path('artists/', ArtistList.as_view(), name='artist-list'),
    path('works/', WorkList.as_view(), name='work-list'),
    path('register/', register, name='register'),
]