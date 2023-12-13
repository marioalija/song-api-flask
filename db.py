import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS songs;
        """
    )
    conn.execute(
        """
        CREATE TABLE songs (
          id INTEGER PRIMARY KEY NOT NULL,
          title STRING,
          artist STRING,
          album STRING,
          duration STRING
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    songs_seed_data = [
        ("Free Bird", "Lynyrd Skynyrd", "Pronounced Leh-Nerd Skin-Nerd", "9:11"),
        ("American Girl", "Tom Petty", "Tom Petty and the Hearbreakers", "3:33"),
        ("The Unforgiven", "Metallica", "The Black Box", "6:28"),
    ]
    conn.executemany(
        """
        INSERT INTO songs (title, artist, album, duration)
        VALUES (?,?,?,?)
        """,
        songs_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()