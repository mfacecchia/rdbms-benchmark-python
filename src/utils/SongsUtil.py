import os
from typing import List

import requests
from requests.exceptions import HTTPError

from models.Song import Song


class SongsUtil:
    @staticmethod
    def fetch_songs() -> List[Song]:
        playlist_id = "6yPiKpy7evrwvZodByKvM9"
        offset = 100
        host = "spotify23.p.rapidapi.com"
        api_key = os.getenv("RAPIDAPI-SPOTIFY-KEY")
        # Max value allowed by this API
        limit = 100
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
