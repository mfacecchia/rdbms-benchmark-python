from time import perf_counter
from typing import Dict, List

from models.Song import Song
from service.SongService import SongService
from utils.SongsUtil import SongsUtil


class Benchmark:
    _services: List[SongService]
    _results: Dict[str, float]

    def __init__(self, services: List[SongService]):
        self._services = services
        self._results = {}

    def begin_benchmark(self, iterations: int):
        if iterations <= 0:
            raise ValueError("Iterations count cannot be lower than 1.")
        ITEMS_PER_REQUEST = 100
        print("Beginning benchmark...")
        for _ in range(iterations):
            songs: List[Song] = self.__fetch_entries(ITEMS_PER_REQUEST, 1)
            print(
                "Benchmarking for {items_count} items.".format(items_count=len(songs))
            )
            for service in self._services:
                print(
                    "Benchmarking {provider} provider...".format(
                        provider=self.__get_provider(service)
                    )
                )
                self.__benchmark_creation(service, songs)
                self.__benchmark_fetch(service)
                self.__benchmark_delete(service)
                print("Done.")
            print("Done.")

    def __benchmark_creation(self, service: SongService, songs: List[Song]) -> None:
        print("Adding entries...")
        start = self.__get_current_microseconds_time()
        for song in songs:
            service.save(song)
        end = self.__get_current_microseconds_time()
        result = self.__calculate_elapsed_time(start, end)
        self._results.setdefault(
            "Creation-provider-{0}".format(self.__get_provider(service)),
            result,
        )
        print("Done.")

    def __benchmark_delete(self, service: SongService) -> None:
        print("Deleting entries...")
        start = self.__get_current_microseconds_time()
        service.delete_all()
        end = self.__get_current_microseconds_time()
        result = self.__calculate_elapsed_time(start, end)
        self._results.setdefault(
            "Deletion-provider-{0}".format(self.__get_provider(service)), result
        )
        print("Done.")

    def __benchmark_fetch(self, service: SongService) -> None:
        print("Fetching entries...")
        start = self.__get_current_microseconds_time()
        entries = service.find_all()
        end = self.__get_current_microseconds_time()
        result = self.__calculate_elapsed_time(start, end)
        self._results.setdefault(
            "Fetch-provider-{0}".format(self.__get_provider(service)), result
        )
        print("Done.")
        print("Fetched {0} entries".format(len(entries)))

    def __get_current_microseconds_time(self) -> float:
        return perf_counter()

    def __calculate_elapsed_time(self, start: float, end: float) -> float:
        total_seconds: float = end - start
        if total_seconds < 0:
            raise ValueError(
                "End time comes before start time. Cannot evaluate benchmark results"
            )
        return total_seconds

    def get_results(self) -> Dict[str, float]:
        return self._results

    def __get_provider(self, service: SongService) -> str:
        return service.get_conn().get_db_name()

    def __fetch_entries(self, results: int, page: int) -> List[Song]:
        if page <= 0:
            raise ValueError("Page cannot be lower than 1.")
        if results <= 0:
            raise ValueError("Results count cannot be lower than 1.")
        print("Fetching entries...")
        total_fetched: int = 0
        fetched_songs: List[Song] = []
        while total_fetched >= results:
            res: List[Song] = SongsUtil.fetch_songs(100, page)
            # Quitting in case the API returns no other elements (avoiding infinite loop)
            if len(res) == 0:
                break
            fetched_songs += res
            total_fetched += len(res)
            page += 1
        return fetched_songs
