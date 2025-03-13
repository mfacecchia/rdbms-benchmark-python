from typing import Any, LiteralString

from psycopg import connect, sql
from psycopg.rows import TupleRow
from psycopg.sql import Composed

from ctyping.postgresql import TPostgreSqlConnection
from utils.Environment import Environment

from .DatabaseConnection import DatabaseConnection


class PostgreSql(DatabaseConnection[TPostgreSqlConnection]):
    _conn: TPostgreSqlConnection | None

    def __init__(self):
        super().__init__("PostgreSql")
        self._conn = None

    def execute(
        self,
        conn: TPostgreSqlConnection,
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

    def connect(self) -> TPostgreSqlConnection:
        if self._conn is None or self._conn.closed:
            self._conn = connect(
                dbname="rdbms_benchmark",
                autocommit=True,
                host=Environment.get_environment_variable("POSTGRES_HOST"),
                port=Environment.get_environment_variable("POSTGRES_PORT"),
                user=Environment.get_environment_variable("POSTGRES_USER"),
                password=Environment.get_environment_variable("POSTGRES_PASSWORD"),
            )
        return self._conn

    def close(self) -> None:
        if self._conn is None:
            return
        self._conn.close()
