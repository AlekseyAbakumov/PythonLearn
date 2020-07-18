from tempfile import gettempdir
from os.path import join, exists
from random import randrange


class File(object):
    """Class for working with files (read, write, add)
    Supports iteration protocol by file lines
    """
    def __init__(self, path_to_file):
        """Open or create a file with a given path
        :param path_to_file:    str with path to file
        """
        if not exists(path_to_file):
            with open(path_to_file, 'w') as f:
                pass
        self.file_path = path_to_file

    def __str__(self):
        return self.file_path

    def __add__(self, other) -> object:
        """Create File object by adding contents of file 2 to the contents
        of file 1. New file created it temp dir.
        :param other:   second file object to merge
        :return:        resulting new file object
        """
        filename = join(gettempdir(), f"tempfile_{str(randrange(999))}.txt")
        # guessing until filename not exists
        while exists(filename):
            filename = join(gettempdir(), f"tempfile_{str(randrange(999))}.txt")
        new_file_object = File(filename)
        new_file_object.write(self.read() + other.read())
        return new_file_object

    def __iter__(self):
        with open(self.file_path) as f:
            for line in f:
                yield line

    def read(self) -> str:
        """Reads the whole file and return a string with its content
        :return:                str with file contents
        """
        with open(self.file_path, 'r') as f:
            return f.read()

    def write(self, new_content: str):
        """Writes 'new_content' to the file (overwriting, not appending)
        :param new_content: str with new content
        """
        with open(self.file_path, 'w') as f:
            return f.write(new_content)