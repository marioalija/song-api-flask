import db
from models import Artist, Song


db.create_all()

artist = Artist.query.get(1)
song = Song.query.get(1)

artist.songs.append(song)
db.session.commit()