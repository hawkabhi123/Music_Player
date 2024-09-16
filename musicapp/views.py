from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

from .models import Favourite, Playlist, Recent, Song


# Create your views here.
def landing(request):
    return render(request, "musicapp/landing.html")


def explore(request):
    if not request.user.is_anonymous:
        recent = list(
            Recent.objects.filter(user=request.user).values("song_id").order_by("-id")
        )
        recent_id = [each["song_id"] for each in recent][:10]
        recent_songs_unsorted = Song.objects.filter(
            id__in=recent_id, recent__user=request.user
        )
        recent_songs = list()
        for id in recent_id:
            recent_songs.append(recent_songs_unsorted.get(id=id))
    else:
        recent = None
        recent_songs = None

    first_time = False
    last_played_song = None

    if not request.user.is_anonymous:
        last_played_list = list(
            Recent.objects.filter(user=request.user).values("song_id").order_by("-id")
        )

        if last_played_list:
            last_played_id = last_played_list[0]["song_id"]
            last_played_song = Song.objects.get(id=last_played_id)
        else:
            first_time = True

    else:
        first_time = True

    if not request.user.is_anonymous and request.method == "POST":
        if "play" in request.POST:
            song_id = request.POST["play"]
            song = Song.objects.filter(id=song_id).first()
            if list(Recent.objects.filter(song=song, user=request.user).values()):
                query = Recent.objects.filter(song=song, user=request.user)
                query.delete()
            
            query = Recent(song=song, user=request.user)
            query.save()
            return redirect("explore")


    songs_all = list(Song.objects.all().values("id").order_by("?"))
    sliced_ids = [each["id"] for each in songs_all][:10]
    explore_all_songs = Song.objects.filter(id__in=sliced_ids)

    songs_hindi = list(Song.objects.all().filter(language="Hindi").values("id"))
    sliced_ids = [each["id"] for each in songs_hindi][:10]
    explore_hindi_songs = Song.objects.filter(id__in=sliced_ids)

    songs_punjabi = list(Song.objects.all().filter(language="Punjabi").values("id"))
    sliced_ids = [each["id"] for each in songs_punjabi][:10]
    explore_punjabi_songs = Song.objects.filter(id__in=sliced_ids)

    songs_haryanvi = list(Song.objects.all().filter(language="Haryanvi").values("id"))
    sliced_ids = [each["id"] for each in songs_haryanvi][:10]
    explore_haryanvi_songs = Song.objects.filter(id__in=sliced_ids)

    songs_english = list(Song.objects.all().filter(language="English").values("id"))
    sliced_ids = [each["id"] for each in songs_english][:10]
    explore_english_songs = Song.objects.filter(id__in=sliced_ids)

    songs_assamese = list(Song.objects.all().filter(language="Assamese").values("id"))
    sliced_ids = [each["id"] for each in songs_assamese][:10]
    explore_assamese_songs = Song.objects.filter(id__in=sliced_ids)

    songs_bhojpuri = list(Song.objects.all().filter(language="Bhojpuri").values("id"))
    sliced_ids = [each["id"] for each in songs_bhojpuri][:10]
    explore_bhojpuri_songs = Song.objects.filter(id__in=sliced_ids)

    context = {
        "all_songs": explore_all_songs,
        "recent_songs": recent_songs,
        "hindi_songs": explore_hindi_songs,
        "english_songs": explore_english_songs,
        "punjabi_songs": explore_punjabi_songs,
        "haryanvi_songs": explore_haryanvi_songs,
        "assamese_songs": explore_assamese_songs,
        "bhojpuri_songs": explore_bhojpuri_songs,
        "last_played_song": last_played_song,
        "first_time": first_time,
        "query_search": False,
    }

    return render(request, "musicapp/explore.html", context=context)


def all_songs(request):
    songs = Song.objects.all()

    last_played_song = None
    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.filter(user=request.user).values("song_id").order_by("-id"))

        if last_played_list:
            last_played_id = last_played_list[0]["song_id"]
            last_played_song = Song.objects.get(id=last_played_id)

    if request.method == "POST":
        if "play" in request.POST:
            song_id = request.POST["play"]
            song = Song.objects.filter(id=song_id).first()
            if list(Recent.objects.filter(song=song, user=request.user).values()):
                query = Recent.objects.filter(song=song, user=request.user)
                query.delete()
            
            query = Recent(song=song, user=request.user)
            query.save()
            return redirect("all-songs")
    
    context = {
        "all_songs": songs,
        "last_played_song": last_played_song,
    }

    return render(request, "musicapp/all-songs.html", context=context)


def hindi_songs(request):
    songs = Song.objects.all().filter(language="Hindi")

    last_played_song = None
    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.filter(user=request.user).values("song_id").order_by("-id"))

        if last_played_list:
            last_played_id = last_played_list[0]["song_id"]
            last_played_song = Song.objects.get(id=last_played_id)

    if request.method == "POST":
        if "play" in request.POST:
            song_id = request.POST["play"]
            song = Song.objects.filter(id=song_id).first()
            if list(Recent.objects.filter(song=song, user=request.user).values()):
                query = Recent.objects.filter(song=song, user=request.user)
                query.delete()
            
            query = Recent(song=song, user=request.user)
            query.save()
            return redirect("hindi-songs")

    context = {
        "hindi_songs": songs,
        "last_played_song": last_played_song,
    }

    return render(request, "musicapp/hindi-songs.html", context=context)


def english_songs(request):
    songs = Song.objects.all().filter(language="English")

    last_played_song = None

    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.filter(user=request.user).values("song_id").order_by("-id"))

        if last_played_list:
            last_played_id = last_played_list[0]["song_id"]
            last_played_song = Song.objects.get(id=last_played_id)

    if request.method == "POST":
        if "play" in request.POST:
            song_id = request.POST["play"]
            song = Song.objects.filter(id=song_id).first()
            if list(Recent.objects.filter(song=song, user=request.user).values()):
                query = Recent.objects.filter(song=song, user=request.user)
                query.delete()
            
            query = Recent(song=song, user=request.user)
            query.save()
            return redirect("english-songs")
    
    context = {
        "english_songs": songs,
        "last_played_song": last_played_song,
    }

    return render(request, "musicapp/english-songs.html", context=context)

def punjabi_songs(request):
    songs = Song.objects.all().filter(language="Punjabi")

    last_played_song = None

    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.filter(user=request.user).values("song_id").order_by("-id"))

        if last_played_list:
            last_played_id = last_played_list[0]["song_id"]
            last_played_song = Song.objects.get(id=last_played_id)

    if request.method == "POST":
        if "play" in request.POST:
            song_id = request.POST["play"]
            song = Song.objects.filter(id=song_id).first()
            if list(Recent.objects.filter(song=song, user=request.user).values()):
                query = Recent.objects.filter(song=song, user=request.user)
                query.delete()
            
            query = Recent(song=song, user=request.user)
            query.save()
            return redirect("punjabi-songs")
    
    context = {
        "punjabi_songs": songs,
        "last_played_song": last_played_song,
    }

    return render(request, "musicapp/punjabi-songs.html", context=context)

def haryanvi_songs(request):
    songs = Song.objects.all().filter(language="Haryanvi")

    last_played_song = None

    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.filter(user=request.user).values("song_id").order_by("-id"))

        if last_played_list:
            last_played_id = last_played_list[0]["song_id"]
            last_played_song = Song.objects.get(id=last_played_id)

    if request.method == "POST":
        if "play" in request.POST:
            song_id = request.POST["play"]
            song = Song.objects.filter(id=song_id).first()
            if list(Recent.objects.filter(song=song, user=request.user).values()):
                query = Recent.objects.filter(song=song, user=request.user)
                query.delete()
            
            query = Recent(song=song, user=request.user)
            query.save()
            return redirect("haryanvi-songs")
    
    context = {
        "haryanvi_songs": songs,
        "last_played_song": last_played_song,
    }

    return render(request, "musicapp/haryanvi-songs.html", context=context)

def assamese_songs(request):
    songs = Song.objects.all().filter(language="Assamese")

    last_played_song = None

    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.filter(user=request.user).values("song_id").order_by("-id"))

        if last_played_list:
            last_played_id = last_played_list[0]["song_id"]
            last_played_song = Song.objects.get(id=last_played_id)

    if request.method == "POST":
        if "play" in request.POST:
            song_id = request.POST["play"]
            song = Song.objects.filter(id=song_id).first()
            if list(Recent.objects.filter(song=song, user=request.user).values()):
                query = Recent.objects.filter(song=song, user=request.user)
                query.delete()
            
            query = Recent(song=song, user=request.user)
            query.save()
            return redirect("assamese-songs")
    
    context = {
        "assamese_songs": songs,
        "last_played_song": last_played_song,
    }

    return render(request, "musicapp/assamese-songs.html", context=context)

def bhojpuri_songs(request):
    songs = Song.objects.all().filter(language="Bhojpuri")

    last_played_song = None

    if not request.user.is_anonymous:
        last_played_list = list(Recent.objects.filter(user=request.user).values("song_id").order_by("-id"))

        if last_played_list:
            last_played_id = last_played_list[0]["song_id"]
            last_played_song = Song.objects.get(id=last_played_id)

    if request.method == "POST":
        if "play" in request.POST:
            song_id = request.POST["play"]
            song = Song.objects.filter(id=song_id).first()
            if list(Recent.objects.filter(song=song, user=request.user).values()):
                query = Recent.objects.filter(song=song, user=request.user)
                query.delete()
            
            query = Recent(song=song, user=request.user)
            query.save()
            return redirect("bhojpuri-songs")
    
    context = {
        "bhojpuri_songs": songs,
        "last_played_song": last_played_song,
    }

    return render(request, "musicapp/bhojpuri-songs.html", context=context)

def search(request):

    filtered_songs = None

    if len(request.GET) > 0:
        search_query = request.GET.get("q")
        filtered_songs = (
            Song.objects.all().filter(Q(name__icontains=search_query)).distinct()
        )

    context = {
        "search_results": filtered_songs,
        "query_search": True,
    }
    return render(request, "musicapp/search.html", context=context)


@login_required(login_url="login")
def mymusic(request):
    playlists = (Playlist.objects.filter(user=request.user).values("playlist").distinct())[:7]
    
    fav_songs = Song.objects.filter(favourite__user=request.user, favourite__is_fav=True).distinct()[:7][::-1]

    recent = list(Recent.objects.filter(user=request.user).values("song_id").order_by("-id"))
    recent_id = [each["song_id"] for each in recent][:7]
    recent_songs_unsorted = Song.objects.filter(id__in=recent_id, recent__user=request.user)
    recent_songs = list()
    for id in recent_id:
        recent_songs.append(recent_songs_unsorted.get(id=id))

    last_played_song = None
    last_played_list = list(Recent.objects.filter(user=request.user).values("song_id").order_by("-id"))

    if last_played_list:
        last_played_id = last_played_list[0]["song_id"]
        last_played_song = Song.objects.get(id=last_played_id)

    if request.method == "POST":
        if "play" in request.POST:
            song_id = request.POST["play"]
            song = Song.objects.filter(id=song_id).first()
            if list(Recent.objects.filter(song=song, user=request.user).values()):
                query = Recent.objects.filter(song=song, user=request.user)
                query.delete()
            
            query = Recent(song=song, user=request.user)
            query.save()
            return redirect("mymusic")

    context = {
        "playlists": playlists,
        "fav_songs": fav_songs,
        "recent_songs": recent_songs,
        "last_played_song": last_played_song,
    }

    return render(request, "musicapp/mymusic.html", context=context)


@login_required(login_url="login")
def myplaylists(request):
    playlists = (Playlist.objects.filter(user=request.user).values("playlist").distinct())
    context = {
        "playlists": playlists,
    }

    return render(request, "musicapp/my-playlists.html", context=context)


@login_required(login_url="login")
def playlist(request, playlist_name):
    playlist_songs = Song.objects.filter(playlist__playlist=playlist_name, playlist__user=request.user).distinct()[::-1]

    if request.method == "POST":
        print(request.POST)
        if 'rm-playlist' in request.POST:
            song_id = request.POST["rm-playlist"]
            playlist_song = Playlist.objects.filter(playlist=playlist_name, song__id=song_id, user=request.user)
            playlist_song.delete()
            return redirect("playlist", playlist_name=playlist_name)

    context = {
        "playlist_name": playlist_name,
        "playlist_songs": playlist_songs,
        "playlist_count": len(playlist_songs),
    }

    return render(request, "musicapp/playlist.html", context=context)


@login_required(login_url="login")
def liked_songs(request):
    songs = list(Song.objects.filter(favourite__user=request.user, favourite__is_fav=True).distinct())[::-1]

    if request.method == "POST":
        # print(request.POST)
        song_id = request.POST["rm-fav"]
        if "rm-fav" in request.POST:
            query = Favourite.objects.filter(user=request.user, song=song_id, is_fav=True)
            print(f"query: {query}")
            query.delete()
            return redirect("liked-songs")
    
    context = {
        "liked_songs": songs,
        "liked_count": len(songs),
    }
    return render(request, "musicapp/liked-songs.html", context=context)


@login_required(login_url="login")
def recently_played(request):
    recent = list(
        Recent.objects.filter(user=request.user).values("song_id").order_by("-id")
    )
    recent_id = [each["song_id"] for each in recent]
    recent_songs_unsorted = Song.objects.filter(
            id__in=recent_id, recent__user=request.user
        )
    recent_songs = list()
    for id in recent_id:
        recent_songs.append(recent_songs_unsorted.get(id=id))
    
    context = {
        "recent_songs":recent_songs[:30],
    }

    return render(request, "musicapp/recently-played.html", context=context)


@login_required(login_url="login")
def details(request, song_id):
    print(request.path)
    song = Song.objects.filter(id=song_id).first()

    is_favourite = (
        Favourite.objects.filter(user=request.user)
        .filter(song=song_id)
        .values("is_fav")
    )
    artists = list(song.artists.split(","))
    playlists = Playlist.objects.filter(user=request.user).values("playlist").distinct()

    last_played_song = None
    last_played_list = list(Recent.objects.values("song_id").order_by("-id"))
    if last_played_list:
        last_played_id = last_played_list[0]["song_id"]
        last_played_song = Song.objects.get(id=last_played_id)
    

    if request.method == "POST":
        print(request.POST)
        if "add-fav" in request.POST:
            query = Favourite.objects.filter(user=request.user, song=song, is_fav=True)
            if not query:
                query = Favourite(user=request.user, song=song, is_fav=True)
                print(f"query: {query}")
                query.save()
           
            return redirect("details", song_id=song_id)

        if "rm-fav" in request.POST:
            query = Favourite.objects.filter(user=request.user, song=song, is_fav=True)
            print(f"query: {query}")
            query.delete()
            return redirect("details", song_id=song_id)

        if "playlist" in request.POST:
            playlist_name = request.POST["playlist"]
            query = Playlist.objects.filter(user=request.user, song=song, playlist=playlist_name)
            if not query.exists():
                query = Playlist(user=request.user, song=song, playlist=playlist_name)
                query.save()
            return redirect("details", song_id=song_id)

        if "play-song" in request.POST:
            song = Song.objects.filter(id=song_id).first()
            if list(Recent.objects.filter(song=song, user=request.user).values()):
                query = Recent.objects.filter(song=song, user=request.user)
                query.delete()
            
            query = Recent(song=song, user=request.user)
            query.save()
            return redirect("details", song_id=song_id)

    # for playlist in playlists.iterator():
    #     playlist_count = Song.objects.filter(
    #         playlist__playlist=playlist.playlist, playlist__user=request.user
    #     ).count()
    #     print(playlist_count)

    context = {
        "song": song,
        "is_favourite": is_favourite,
        "artists": artists,
        "playlists": playlists,
        "last_played_song": last_played_song,
    }

    return render(request, "musicapp/details.html", context=context)
