from typing import Any, LiteralString

from DatabaseConnection import DatabaseConnection
from psycopg import Connection, connect, sql
from psycopg.rows import TupleRow
from psycopg.sql import Composed


class PostgreSql(DatabaseConnection[Connection[TupleRow]]):
    def execute(
        self,
        conn: Connection[TupleRow],
        query: LiteralString,
        table_name: str,
        fields: list[str],
        data: list[Any],
        get_query_result: bool,
    ) -> list[TupleRow] | None:
        formattedQuery: Composed = sql.SQL(query).format(
            table=sql.Identifier(table_name),
            fields=sql.SQL(",").join(map(sql.Identifier, fields)),
        )
        with conn.cursor() as cur:
            if get_query_result is True:
                return cur.execute(formattedQuery, data).fetchall()
            cur.execute(formattedQuery, data)

    def connect(self) -> Connection[TupleRow]:
        return connect(dbname="rdbms_benchmark", user="feis._.", autocommit=False)
