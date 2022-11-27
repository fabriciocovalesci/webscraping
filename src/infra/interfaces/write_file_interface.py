from abc import ABC, abstractmethod
from ...contract.contract import Contract

class WriteFileInterface(ABC):
    
    @abstractmethod
    def write(cls, object: Contract):
        pass