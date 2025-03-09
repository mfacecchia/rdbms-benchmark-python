from typing import Any

from databases.DatabaseConnection import DatabaseConnection


class DbUtil:
    @staticmethod
    def get_last_generated_value(
        conn: DatabaseConnection[Any], table_name: str, pk: str
    ) -> int:
        query = "SELECT MAX({fields}) from {table}"
        return conn.execute(conn.connect(), query, table_name, [pk], [], True)[0][0]
