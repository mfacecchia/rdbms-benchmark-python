class Song:
    _id: int
    _title: str
    _artist_name: str
    _is_explicit: bool
    _duration: int

    def __init__(self):
        self._id = 0
        self._title = ""
        self._artist_name = ""
        self._is_explicit = False
        self._duration = 0

    def get_id(self) -> int:
        return self._id

    def set_id(self, value: int) -> None:
        self._id = value

    def get_title(self) -> str:
        return self._title

    def set_title(self, value: str) -> None:
        self._title = value

    def get_artist_name(self) -> str:
        return self._artist_name

    def set_artist_name(self, value: str) -> None:
        self._artist_name = value

    def get_is_explicit(self) -> bool:
        return self._is_explicit

    def set_is_explicit(self, value: bool) -> None:
        self._is_explicit = value

    def get_duration(self) -> int:
        return self._duration

    def set_duration(self, duration: int) -> None:
        self._duration = duration

    def __str__(self) -> str:
        return f"Song(id={self._id}, title='{self._title}', artist_name='{self._artist_name}', is_explicit={self._is_explicit}, duration={self._duration})"
