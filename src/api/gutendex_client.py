# src/api/gutendex_client.py
import time
import requests
from src.api.interfaces import APIClient

class GutendexAPIClient(APIClient):
    def __init__(self):
        self.base_url = ""

    def fetch_data(self, limit=10):
        results = []
        url = self.base_url
        while url and len(results) < limit:
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                results.extend(data.get("results", []))
                
                time.sleep(0.5)
            except requests.RequestException as e:
                print(f"Error al obtener datos: {e}")
                break
        return results[:limit]
