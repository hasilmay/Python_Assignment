#Abstract Base Class (ABC) File handler
from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

class TextHandler(FileHandler):
    def read(self):
        return "Reading text data from file."

    def write(self, data):
        print(f"Writing text data to file: {data}")

class BinaryFileHandler(FileHandler):
    def read(self):
        return "Reading binary data from file."
    def write(self, data):
        print(f"Writing binary data to file: {data}")

txt_handler = TextHandler()
print(txt_handler.read())
txt_handler.write("Hello World")

bin_handler = BinaryFileHandler()
print(bin_handler.read())
bin_handler.write(b"\x00\x01\x02\x03")