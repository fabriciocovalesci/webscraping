import csv
from datetime import datetime
from .interfaces.write_file_interface import WriteFileInterface
from ..contract.contract import Contract
from ..config.logs import Logger
from src.paths import SAVED_DATA

class WriteFile(WriteFileInterface):
    
    def __init__(self):
        self.__header = ["nome", "capital", "populacao", "area"]
        self.__today = datetime.strftime(datetime.today(), "%Y-%m-%d")
    
    def write(self, object: Contract):
        try:
            Logger.logr.info("Initializing module to save data")
            with open(f"{SAVED_DATA}/{self.__today}.csv", 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(self.__header)
                writer.writerows([*object])
            Logger.logr.info(f"Data successfully saved to file {self.__today}.csv in folder data")
        except IOError as e:
            Logger.logr.error(f"{e}")