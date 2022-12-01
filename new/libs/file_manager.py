import re


def sanitize_file_name(filename: str) -> str:
    """
    Removes any invalid character from the given filename.
    :param filename: filename to sanitize
    :return: sanitized filename
    """
    invalid_chars = r'[/:*?"<>\\|]'
    return re.sub(invalid_chars, "", filename)
