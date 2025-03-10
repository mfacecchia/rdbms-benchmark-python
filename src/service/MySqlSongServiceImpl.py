from typing import List

from databases.MySql import MySql
from models.Song import Song
from repository.MySqlSongRepositoryImpl import (
    MySqlSongRepositoryImpl as MySqlSongRepository,
)
from service.SongService import SongService


class MySqlSongServiceImpl(SongService):
    _conn: MySql
    _song_repository: MySqlSongRepository

    def __init__(self):
        self._conn = MySql()
        self._song_repository = MySqlSongRepository()

    def find_all(self) -> List[Song]:
        return self._song_repository.find_all(self._conn)

    def delete_all(self) -> None:
        self._song_repository.delete_all(self._conn)

    def save(self, song: Song) -> None:
        self._song_repository.save(self._conn, song)
