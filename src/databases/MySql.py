from typing import Any, Dict, List, LiteralString

import mysql.connector
from mysql.connector.types import RowItemType, RowType

from ctyping.mysql import TMySqlConnection
from utils.Environment import Environment

from .DatabaseConnection import DatabaseConnection


class MySql(DatabaseConnection[TMySqlConnection]):
    _conn: TMySqlConnection | None

    def __init__(self):
        super().__init__("MySql")
        self._conn = None

    def execute(
        self,
        conn: TMySqlConnection,
        query: LiteralString,
        table_name: str,
        fields: list[str],
        data: list[Any],
        get_query_result: bool,
    ) -> List[RowType | Dict[str, RowItemType]] | None:
        formattedQuery: str = query.format(
            table=table_name,
            fields=",".join(fields),
        )
        with conn.cursor(prepared=True) as cur:
            cur.execute(formattedQuery, data)
            if get_query_result:
                return cur.fetchall()

    def connect(self) -> TMySqlConnection:
        if self._conn is None or self._conn.is_connected:
            self._conn = mysql.connector.connect(
                host=Environment.get_environment_variable("MYSQL_HOST"),
                port=Environment.get_environment_variable("MYSQL_PORT"),
                user=Environment.get_environment_variable("MYSQL_USER"),
                password=Environment.get_environment_variable("MYSQL_PASSWORD"),
                database="rdbms_benchmark",
                autocommit=True,
            )
        return self._conn

    def close(self) -> None:
        if self._conn is None:
            return
        self._conn.close()
