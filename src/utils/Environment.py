from os import getenv

from dotenv import load_dotenv


class Environment:
    @staticmethod
    def get_environment_variable(key: str) -> str:
        load_dotenv()
        value = getenv(key)
        if value is None:
            raise ValueError("Value not found for key {k}".format(k=key))
        return value
