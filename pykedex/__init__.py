"""Top-level package for Pykedex"""

__app_name__ = "pykedex"
__version__ = "0.1.0"

(
    SUCCESS,
    API_ERROR,
    ID_ERROR,
    STRING_ERROR,
    DB_WRITE_ERROR,
    DIR_ERROR,
    FILE_ERROR,
) = range(7)

ERRORS = {
    API_ERROR: "API endpoint error",
    ID_ERROR: "Invalid ID error",
    STRING_ERROR: "Invalid String/Name error",
}