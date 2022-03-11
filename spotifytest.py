import spotipy
from spotipy.oauth2 import SpotifyOAuth



SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth('a620a32c5e2644edb56292724f8711f0','e9152986f5644c6d8acefd8002e236c8','https://open.spotify.com/', scope=SCOPE, cache_path=CACHE))


results = sp.playlist_items('https://open.spotify.com/playlist/4NKQC01pmUYlJqSRQnWTVL')

for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
    print('cover art: ' + track['album']['images'][0]['url'])