import random
import os

import spotipy
import spotipy.util as util

def select_random_album(artist):
    results = spotify.artist_albums(artist)
    albums = results['items']
    return random.choice(albums)

def album_tracks(album_uri):
    tonights_tracks = spotify.album_tracks(album_uri)
    return [track['uri'] for track in tonights_tracks['items']]

tkkg_retro_archiv_uri = "spotify:artist:0i38tQX5j4gZ0KS3eCMoIl"

user_id = "datosh-de"
artist_uri = tkkg_retro_archiv_uri
nightynight_playlist_id = "spotify:playlist:39lHlXSt2NkOVmtVkLgALd"

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(user_id, scope)
spotify = spotipy.Spotify(auth=token)

tonights_album = select_random_album(artist_uri)
tracks = album_tracks(tonights_album['uri'])

result = spotify.user_playlist_replace_tracks(
    user_id,
    nightynight_playlist_id,
    tracks)
