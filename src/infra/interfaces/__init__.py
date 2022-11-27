from abc import ABC, abstractmethod
from typing import Dict

class InfraInterface(ABC):

    @abstractmethod
    def write_value(self) -> Dict[int, str]:
        pass