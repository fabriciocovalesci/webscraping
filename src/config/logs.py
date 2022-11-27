import logging.config
from src.paths import LOG_CONFIG

def singleton(cls):
    instances = {}
    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance()

@singleton
class Logger():
    def __init__(self):
        logging.config.fileConfig(LOG_CONFIG)
        self.logr = logging.getLogger('root')