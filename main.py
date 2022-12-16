"""
File manipulation lib

Author: Christian M. Fulton
Date: 03.Nov.2021
"""
import shutil
import os
from json import dumps
from json import loads


class Manage:
    """
    File lib

    :Use: Instantiate file object { fileobj = Manage('name') }
        -> Work with fileobj
    
    Parameter title: Title of the file to work with.
    Parameter save: Saves the file(as .txt by default)
    Preconditions: title must be a valid string following os naming convention.
    """
    def __init__(self, title: str, save=True):
        self.title: str = title
        self.save: bool = save
        self.ext: str = ''
        #loc = os.path
        if save:
            # check to see if file exists: if file exists -> don't save
            if self.title in os.listdir(): 
                print(f'Working with existing file: {self.title}')
            else:
                self.make_file()
    
    def name(self) -> str:
        """
        Return the name of the file with the extension.
        """
        return self.title + self.ext
    
    def make_file(self, ext='.txt') -> None:
        """
        Make file if it doesn't exist
        file extension default - .txt
        TODO: Ability to save to path..
        """
        if not ext.startswith('.'):
            ext = f'.{ext}'
        if self.title in os.listdir():
            print('File already exists...')
        else:
            self.ext = ext
            fname = open(self.title, 'wt')
            fname.close()
    
    def write_line(self, data: str) -> None:
        """
        Append existing file with single line
        """
        with open(self.title, 'a') as rfile:
            rfile.write(data + '\n')
    
    def write_data(self, data: str) -> None:
        """
        Write data: should be tuple | list
        """
        NotImplementedError
    
    def read_me(self) -> None:
        """
        Read the file
        """
        with open(self.title, 'r') as rfile:
            for line in rfile:
                print(line)

    def move_me(self, dst: str) -> None:
        """
        Move file around
        Parameter dst:
        Preconditions:
        """
        # if you're moving the file, you have to move with it 
        #   || have a pointer -> file
        # if dst == '..' -> move up 1 level
        if dst == '..':
            dst = os.path.abspath(os.path.join('.', os.pardir))
        try:
            shutil.move(self.title, dst)
        except Exception:
            print(f'An error occurred when trying to move {self.title}')

    def read_counter(self):
        if os.path.exists('counter.json'):
            return loads(open('counter.json'), 'r') + 1
    
    def write_counter(self) -> None:
        counter = self.read_counter()
        with open('counter.json', 'w') as rfile:
            rfile.write(dumps(counter))

class Fthis:
    """
    play with fs
    """
    NotImplementedError