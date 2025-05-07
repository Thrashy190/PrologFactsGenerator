# src/formatters/interfaces.py
from abc import ABC, abstractmethod

class DataFormatter(ABC):
    @abstractmethod
    def format_to_facts(self, items):
        pass
