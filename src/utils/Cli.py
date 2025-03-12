from sys import argv


class Cli:
    """
    A CLI utility class for handling command line arguments.

    This class provides static methods to parse and retrieve command line arguments
    based on specified flags.
    """

    @staticmethod
    def get_argument(flag: str, required: bool):
        """
        Takes an argument from the command line followed by the passed `flag`

        Returns:
            `str`: the found flag value

        Throws:
            `ValueError`: if there is no value linked to that flag or the flag is not found at all
        """
        for i, arg in enumerate(argv):
            if arg == flag:
                try:
                    return argv[i + 1]
                except IndexError:
                    raise ValueError(f"Invalid value for the required {flag} flag.")
        if required is True:
            raise ValueError("Flag {flag} not provided.")
        return None
