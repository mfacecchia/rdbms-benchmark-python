from typing import List

import requests
from requests.exceptions import HTTPError

from models.Song import Song
from utils.Environment import Environment


class SongsUtil:
    @staticmethod
    def fetch_songs(songs_count: int, page: int) -> List[Song]:
        if songs_count <= 0 or page <= 0:
            raise ValueError("Songs count or page cannot be lower than 1.")
        if songs_count > 100:
            raise ValueError(
                "Songs count cannot be higher than 100 due to API constraints."
            )
        playlist_id = "6yPiKpy7evrwvZodByKvM9"
        offset = page
        host = "spotify23.p.rapidapi.com"
        api_key = Environment.get_environment_variable("RAPIDAPI-SPOTIFY-KEY")
        limit = songs_count
        res = requests.get(
            str.format(
                "https://spotify23.p.rapidapi.com/playlist_tracks/?id={playlist_id}&offset={offset}&limit={limit}",
                playlist_id=playlist_id,
                offset=offset,
                limit=limit,
            ),
            headers={
                "content-type": "application/json",
                "x-rapidapi-host": host,
                "x-rapidapi-key": api_key,
            },
        )
        if not res.ok:
            raise HTTPError(
                str.format(
                    "Server responses with a {status} HTTP status code",
                    status=res.status_code,
                )
            )
        items = res.json()["items"]

        songs: List[Song] = []

        for entry in items:
            track = entry["track"]

            song = Song()
            song.set_title(track["name"])
            song.set_is_explicit(track["explicit"])
            song.set_artist_name(track["artists"][0]["name"])
            song.set_duration(track["duration_ms"] / 1000)
            songs.append(song)

        return songs
