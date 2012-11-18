from subprocess import call
from gbots.util.pynix import convert_to_posix_args

def save_web_page_complete(url, where=None, **kwargs):
    """
    Use wget to grab all the content and static resources of a web page and save them
    relative to `where`

    @param url: the url to web page to store
    @param where: all resources are stored relative to here
    @param kwargs: any additional keyword arguments for wget
    @return: False if any errors occurred during this process
    """
    extra_args = convert_to_posix_args(**kwargs)
    return call(
        ("wget", "-E", "-H", "-k", "-K", "-p", "-e", "robots=off", url) + extra_args,
        cwd=None if where is None else str(where)
    ) == 0  # return true if exit code is successful

