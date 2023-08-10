from lib.album import Album

"""
Test instance initates with correct fields
create instance 
assert each filed is correct
"""

def test_album_construct():
    album = Album(1, 'Ice cream', 2005, 3)
    assert album.id == 1
    assert album.title == 'Ice cream'
    assert album.release_year == 2005
    assert album.artist_id == 3    

"""
Can format albums to strings nicely
"""

def test_albums_format_nicely():
    album = Album(1, 'Ice cream', 2005, 3)
    assert str(album) == "Album(1, Ice cream, 2005, 3)"

"""
We can compare two idenetical albums
and have them be equal
"""

def test_albums_are_equal():
    album1 = Album(1, 'Ice cream', 2005, 3)
    album2 = Album(1, 'Ice cream', 2005, 3)
    assert album1 == album2