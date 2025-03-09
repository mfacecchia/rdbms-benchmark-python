from typing import List

from ctyping.postgresql import TPostgreSqlConnection
from databases.DatabaseConnection import DatabaseConnection
from models.Song import Song
from repository.SongRepository import SongRepository
from utils.DbUtil import DbUtil


class PostgreSqlRepositoryImpl(SongRepository):
    def find_all(self, conn: DatabaseConnection[TPostgreSqlConnection]) -> List[Song]:
        query: str = "SELECT * FROM {table};"
        return conn.execute(conn.connect(), query, "song", [], [], True)

    def delete_all(self, conn: DatabaseConnection[TPostgreSqlConnection]) -> None:
        query: str = "DELETE FROM {table};"
        conn.execute(conn.connect(), query, "song", [], [], False)

    def save(self, conn: DatabaseConnection[TPostgreSqlConnection], song: Song) -> None:
        query: str = "INSERT INTO {table} ({fields}) VALUES(%s, %s, %s, %s);"
        conn.execute(
            conn.connect(),
            query,
            "song",
            ["title", "artistname", "isexplicit", "duration"],
            [
                song.get_title(),
                song.get_artist_name(),
                song.get_is_explicit(),
                song.get_duration(),
            ],
            False,
        )
        generated_id: int = DbUtil.get_last_generated_value(conn, "song", "id")
        song.set_id(generated_id)
