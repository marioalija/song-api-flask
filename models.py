from app import db

artist_songs = db.Table('artist_songs',
    db.Column('artist_id', db.Integer, db.ForeignKey('artist.id')),
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'))
)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    bio = db.relationship('Role', secondary=artist_songs, backref=db.backref('users', lazy='dynamic'))

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    artist = db.Column(db.String(50), unique=True, nullable=False)
    album = db.Column(db.String(50), unique=True, nullable=False)
    duration = db.Column(db.Integer(50), unique=True, nullable=False)