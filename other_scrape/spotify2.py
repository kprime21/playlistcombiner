import spotipy
from spotipy.oauth2 import SpotifyOAuth

#uses spotify api to grab the covers as well

SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'
USER_ID = 'a620a32c5e2644edb56292724f8711f0'
HIDDEN_ID = 'e9152986f5644c6d8acefd8002e236c8'
RELOC_URL = 'https://open.spotify.com/'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=USER_ID,client_secret=HIDDEN_ID,redirect_uri=RELOC_URL, scope=SCOPE, cache_path=CACHE))


results = sp.playlist_items('https://open.spotify.com/playlist/4NKQC01pmUYlJqSRQnWTVL')

for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
    print(track['external_urls']['spotify'])
    print('cover art: ' + track['album']['images'][0]['url'])