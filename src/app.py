from pprint import pprint
from typing import List

from benchmark.Benchmark import Benchmark
from databases.MySql import MySql
from databases.PostgreSql import PostgreSql
from repository.MySqlSongRepositoryImpl import (
    MySqlSongRepositoryImpl as MySqlSongRepository,
)
from repository.PostgreSqlSongRepositoryImpl import (
    PostgreSqlSongRepositoryImpl as PostgreSqlSongRepository,
)
from service.SongService import SongService


def main():
    services: List[SongService] = [
        SongService(MySql(), MySqlSongRepository()),
        SongService(PostgreSql(), PostgreSqlSongRepository()),
    ]
    benchmark = Benchmark(services)
    benchmark.begin_benchmark()

    print("----Results----")
    pprint(benchmark.get_results(), indent=4)
    print("---------------")


if __name__ == "__main__":
    main()
