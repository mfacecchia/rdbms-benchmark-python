from typing import List

from models.Song import Song


class SongsUtil:
    # TODO: Make API call here
    @staticmethod
    def fetch_songs() -> List[Song]:
        songs: List[Song] = []
        sample_song: Song = Song()
        sample_song.set_title("Reflections Laughing")
        sample_song.set_artist_name("The Weeknd")
        sample_song.set_is_explicit(True)
        sample_song.set_duration(300)
        songs.append(sample_song)

        return songs
