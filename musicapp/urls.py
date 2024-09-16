from django.urls import path
from . import views

# Add URLConf
urlpatterns = [
    path('', views.landing, name='landing'),
    path('explore/', views.explore, name='explore'),
    path('all-songs/', views.all_songs, name='all-songs'),
    path('hindi-songs/', views.hindi_songs, name='hindi-songs'),
    path('english-songs/', views.english_songs, name='english-songs'),
    path('punjabi-songs/', views.punjabi_songs, name='punjabi-songs'),
    path('assamese-songs/', views.assamese_songs, name='assamese-songs'),
    path('bhojpuri-songs/', views.bhojpuri_songs, name='bhojpuri-songs'),
    path('haryanvi-songs/', views.haryanvi_songs, name='haryanvi-songs'),
    path('search/', views.search, name='search'),
    path('mymusic/', views.mymusic, name='mymusic'),
    path('my-playlists/', views.myplaylists, name='my-playlists'),
    path('my-playlists/<str:playlist_name>/', views.playlist, name='playlist'),
    path('liked-songs/', views.liked_songs, name='liked-songs'),
    path('recently-played/', views.recently_played, name='recently-played'),
    path('song/<int:song_id>/', views.details, name='details'),
]