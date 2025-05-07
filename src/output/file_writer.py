# src/output/file_writer.py
class FileWriter:
    def __init__(self, output_file):
        self.output_file = output_file

    def write(self, facts):
        with open("output/" + self.output_file, 'w', encoding='utf-8') as f:
            for fact in facts:
                f.write(fact + '\n')
