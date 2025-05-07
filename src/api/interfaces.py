# src/api/interfaces.py
from abc import ABC, abstractmethod

class APIClient(ABC):
    @abstractmethod
    def fetch_data(self, limit: int):
        pass
