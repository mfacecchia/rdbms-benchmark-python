from psycopg import Connection
from psycopg.rows import TupleRow

type TPostgreSqlConnection = Connection[TupleRow]
