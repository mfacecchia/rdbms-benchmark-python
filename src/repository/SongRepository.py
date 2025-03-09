from abc import abstractmethod
from typing import Any, List

from databases.DatabaseConnection import DatabaseConnection
from models.Song import Song


class SongRepository:

    @abstractmethod
    def find_all(self, conn: DatabaseConnection[Any]) -> List[Song]:
        pass

    @abstractmethod
    def delete_all(self, conn: DatabaseConnection[Any]) -> None:
        pass

    @abstractmethod
    def save(self, conn: DatabaseConnection[Any], song: Song) -> None:
        pass
