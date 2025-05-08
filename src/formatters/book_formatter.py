# src/formatters/book_formatter.py
from src.formatters.interfaces import DataFormatter

class BookDataFormatter(DataFormatter):
    def clean_text(self, text):
        return text.replace('"', '').replace("'", "").strip()

    def format_to_facts(self, items):
        hechos = []
        # for libro in items:
        #     id_libro = libro['id']
        #     titulo = self.clean_text(libro['title'])
        #     hechos.append(f'titulo({id_libro}, "{titulo}").')

        #     for autor in libro.get('authors', []):
        #         nombre_autor = self.clean_text(autor.get('name', 'Desconocido'))
        #         hechos.append(f'autor({id_libro}, "{nombre_autor}").')
        #         if autor.get('birth_year'):
        #             hechos.append(f'nacimiento("{nombre_autor}", {autor["birth_year"]}).')
        #         if autor.get('death_year'):
        #             hechos.append(f'fallecimiento("{nombre_autor}", {autor["death_year"]}).')

        #     for idioma in libro.get('languages', []):
        #         hechos.append(f'idioma({id_libro}, "{idioma}").')

        #     for genero in libro.get('subjects', []):
        #         hechos.append(f'genero({id_libro}, "{self.clean_text(genero)}").')

        #     for estanteria in libro.get('bookshelves', []):
        #         hechos.append(f'estanteria({id_libro}, "{self.clean_text(estanteria)}").')

        #     hechos.append(f'descargas({id_libro}, {libro.get("download_count", 0)}).')

        #     for formato, enlace in libro.get('formats', {}).items():
        #         if formato.startswith('text/plain'):
        #             hechos.append(f'enlace_texto({id_libro}, "{self.clean_text(enlace)}").')
        #             break

        return hechos