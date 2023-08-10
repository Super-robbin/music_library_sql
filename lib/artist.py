class Artist:
    # It represents a row in the db and also an instance of a single artist.
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, genre, albums = None):
        self.id = id
        self.name = name
        self.genre = genre
        self.albums = albums or []

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    # Basically, if artist1(id, title, genre) = artist2(id, title, genre)
    # this method allows us to match them as equal, and therefore
    # show-up as equal, although they have different instances,
    # cause records inside are the same.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"
