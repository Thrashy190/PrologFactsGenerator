# main.py
from src.api.gutendex_client import GutendexAPIClient
from src.formatters.book_formatter import BookDataFormatter
from src.generator.fact_generator import PrologFactGenerator
from src.output.file_writer import FileWriter

def main():
    client = GutendexAPIClient()
    formatter = BookDataFormatter()
    writer = FileWriter("libros.pl")
    generator = PrologFactGenerator(client, formatter, writer)
    generator.run()

if __name__ == "__main__":
    main()
