from typing import List
from pathlib import Path

class Parser:
    extensions = List[str]
    def valid_extension(extension, self):
        if extension in self.extensions:
            return True
