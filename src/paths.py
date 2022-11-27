import os


def get_root_project():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


LOG_CONFIG = f"{get_root_project()}/src/config/log.ini"

SAVED_DATA = f"{get_root_project()}/data"

if not os.path.exists(SAVED_DATA):
    os.umask(0)
    os.makedirs(SAVED_DATA, mode=0o777)