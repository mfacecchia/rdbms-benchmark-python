from abc import abstractmethod
from typing import Any, LiteralString


class DatabaseConnection[T]:
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
