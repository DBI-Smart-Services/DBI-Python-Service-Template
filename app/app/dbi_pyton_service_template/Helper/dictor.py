
def dictor(data, path, default=None):
    """
    Returns the value from a dictionary for a given path.
    If the path is not found in the dictionary, the default value is returned.


    :param data:        The dictionary to get the value from
    :param path:        The path to get the value for
    :param default:     The default value to return if the path is not found
    :return:
    """
    try:
        path = path.split(".")
        tmp = data
        for key in path:
            tmp = tmp[key]
        return tmp
    except KeyError:
        return default
