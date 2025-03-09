from typing import Any, Dict, List, LiteralString

import mysql.connector
from mysql.connector.types import RowItemType, RowType

from ctyping.mysql import TMySqlConnection

from .DatabaseConnection import DatabaseConnection


class MySql(DatabaseConnection[TMySqlConnection]):
    _conn: TMySqlConnection | None

    def __init__(self):
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
        if self._conn is None:
            self._conn = mysql.connector.connect(
                host="localhost", port="3306", user="root", database="rdbms_benchmark"
            )
        return self._conn
