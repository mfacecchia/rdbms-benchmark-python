from typing import Any, List

from databases.DatabaseConnection import DatabaseConnection
from models.Song import Song
from repository.SongRepository import SongRepository


class SongService:
    _conn: DatabaseConnection[Any]
    _song_repository: SongRepository

    def __init__(self, conn: DatabaseConnection[Any], song_repository: SongRepository):
        self._conn = conn
        self._song_repository = song_repository

    def find_all(self) -> List[Song]:
        return self._song_repository.find_all(self._conn)

    def delete_all(self) -> None:
        self._song_repository.delete_all(self._conn)

    def save(self, song: Song) -> None:
        self._song_repository.save(self._conn, song)

    def get_conn(self) -> DatabaseConnection[Any]:
        return self._conn
