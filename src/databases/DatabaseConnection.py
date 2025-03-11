from abc import abstractmethod
from typing import Any, LiteralString


class DatabaseConnection[T]:
    _db_name: str

    def __init__(self, db_name: str):
        self._db_name = db_name

    @abstractmethod
    def execute(
        self,
        conn: T,
        query: LiteralString,
        table_name: str,
        fields: list[str],
        data: list[Any],
        get_query_result: bool,
    ) -> Any:
        pass

    @abstractmethod
    def connect(self) -> T:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    def get_db_name(self) -> str:
        return self._db_name
