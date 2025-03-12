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
from utils.Cli import Cli


def main():
    services: List[SongService] = [
        SongService(MySql(), MySqlSongRepository()),
        SongService(PostgreSql(), PostgreSqlSongRepository()),
    ]
    iterations = obtain_iterations_count()
    benchmark = Benchmark(services)
    benchmark.begin_benchmark(iterations)

    print("----Results----")
    pprint(benchmark.get_results(), indent=4)
    print("---------------")


def obtain_iterations_count() -> int:
    iterations = Cli.get_argument("--iterations", False)
    if iterations is None:
        return 1
    try:
        return int(iterations)
    except ValueError:
        raise TypeError(
            "Invalid value provided for the iterations flag. Expected int, found {type}".format(
                type=type(iterations)
            )
        )


if __name__ == "__main__":
    main()
