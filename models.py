# from app import db
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_serializer import SerializerMixin
# from sqlalchemy.ext.associationproxy import association_proxy

# db = SQLAlchemy()

# artist_songs = db.Table('artist_songs',
#     db.Column('artist_id', db.Integer, db.ForeignKey('artist.id')),
#     db.Column('song_id', db.Integer, db.ForeignKey('song.id'))
# )

# class Artist(db.Model, SerializerMixin):
#     __tablename__ = 'artists'

#     serialize_rules = ('-artist_songs',)


#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True, nullable=False)
#     bio = db.relationship('Role', secondary=artist_songs, backref=db.backref('users', lazy='dynamic'))
#     artist_songs = db.relationship('ArtistSong', backref='artist', cascade='all, delete, delete-orphan')
#     songs = association_proxy('artist_songs', 'song')

# class Song(db.Model, SerializerMixin):
#     __tablename__ = 'songs'

#     serialize_rules = ('-artist_songs',)


#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50), unique=True, nullable=False)
#     artist = db.Column(db.String(50), unique=True, nullable=False)
#     album = db.Column(db.String(50), unique=True, nullable=False)
#     duration = db.Column(db.Integer(50), unique=True, nullable=False)
#     artist_songs = db.relationship('ArtistSong', backref='song', cascade='all, delete, delete-orphan')
#     artists = association_proxy('artist_songs', 'artist')


# class ArtistSong(db.Model, SerializerMixin):
#     __tablename__ = 'artist_songs'

#     serialize_rules = ('-artist', '-song',)

#     artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), primary_key=True)
#     song_id = db.Column(db.Integer, db.ForeignKey('song.id'), primary_key=True)

# db.create_all()

# artist = Artist.query.filter_by(name='Flask').first()
# flask_artists= artist.songs

# song = Song.query.get(1)
# artist_songs = song.artists

# artist.songs.append(song)
# db.session.commit()