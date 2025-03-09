from typing import Union

from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

type TMySqlConnection = Union[PooledMySQLConnection, MySQLConnectionAbstract]
