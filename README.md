# 📘 Prolog Fact Generator

Generador modular de hechos en Prolog a partir de APIs públicas como Gutendex (libros), PokéAPI (Pokémon), OMDb (películas) y más.

Este proyecto está estructurado para ser fácilmente ampliable con nuevos clientes API y formateadores.

---

## 🚀 Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/Thrashy190/PrologFactsGenerator.git
cd prolog-fact-generator
```

2. **Crear y activar entorno virtual**

```bash
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso básico

Ejecuta el script principal:

```bash
python main.py
```

Esto descargará datos de la API de libros (Gutendex) y generará un archivo `libros.pl` con hechos Prolog.

---

## 🧱 Estructura del proyecto

```
src/
├── api/                # Clientes de APIs
│   ├── gutendex_client.py
│   └── interfaces.py
├── formatters/         # Formateadores de datos
│   ├── book_formatter.py
│   └── interfaces.py
├── generator/
│   └── fact_generator.py
├── output/
│   └── file_writer.py
main.py
```

---

## 🔁 Adaptar a otra API

### 1. Crear nuevo cliente en `src/api/`

```python
# src/api/pokeapi_client.py
from src.api.interfaces import APIClient
import requests

class PokeAPIClient(APIClient):
    def fetch_data(self, limit=100):
        url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()['results']
```

### 2. Crear nuevo formateador en `src/formatters/`

```python
# src/formatters/pokemon_formatter.py
from src.formatters.interfaces import DataFormatter

class PokemonFormatter(DataFormatter):
    def format_to_facts(self, pokemons):
        return [f"pokemon({i}, \"{p['name']}\")." for i, p in enumerate(pokemons)]
```

### 3. Reemplazar en `main.py`

```python
from src.api.pokeapi_client import PokeAPIClient
from src.formatters.pokemon_formatter import PokemonFormatter
```

## 📄 Salida esperada

Archivo `.pl` con hechos Prolog como:

```prolog
titulo(1342, "Pride and Prejudice").
autor(1342, "Jane Austen").
idoma(1342, "en").
descargas(1342, 50000).
```
