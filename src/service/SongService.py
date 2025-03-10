from abc import abstractmethod
from typing import List

from models.Song import Song


class SongService:

    @abstractmethod
    def find_all(self) -> List[Song]:
        pass

    @abstractmethod
    def delete_all(self) -> None:
        pass

    @abstractmethod
    def save(self, song: Song) -> None:
        pass
