from typing import Any, Dict, List, LiteralString, Union

import mysql.connector
from DatabaseConnection import DatabaseConnection
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.types import RowItemType, RowType


class MySql(DatabaseConnection[Union[PooledMySQLConnection, MySQLConnectionAbstract]]):
    def execute(
        self,
        conn: Union[PooledMySQLConnection, MySQLConnectionAbstract],
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

    def connect(self) -> Union[PooledMySQLConnection, MySQLConnectionAbstract]:
        return mysql.connector.connect(
            host="localhost", port="3306", user="root", database="rdbms_benchmark"
        )
