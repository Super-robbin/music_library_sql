from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

# # Connect to the database
# connection = DatabaseConnection()
# connection.connect()

# # Seed with some seed data
# connection.seed("seeds/music_library.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# for artist in artists:
#     print(artist)

# album_repository = AlbumRepository(connection)
# albums = album_repository.all()

# for album in albums:
#     print(album)

# file: app.py
class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print('\nWelcome to the music library manager!')
        print('\nWhat would you like to do?')
        print('1 - List all albums')
        print('2 - List all artists')

        x = input('\nEnter your choice: ')
        if x == "1":
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()
            for album in albums:
                print(f"{album.id}: {album.title} ({album.release_year} {album.artist_id})")
        else:
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")

if __name__ == '__main__':
    app = Application()
    app.run()