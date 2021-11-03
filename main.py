"""
File manipulation library

Author: Christian M. Fulton
Date: 03.Nov.2021
"""


class Manage:
    """
    File lib

    :Use: Instantiate file object { fileobj = Manage('name') }
        -> Work with fileobj
    
    Parameter title:
    Parameter save:
    Preconditions:
    """
    def __init__(self, title, save=True):
        self.title = title
        self.save = save
        if save:
            self.make_file()
    
    def make_file(self, ext='.txt'):
        """
        Make file if it doesn't exist
        file extension default - .txt
        TODO: Ability to save to path..
        """
        if not ext.startswith('.'):
            ext = '.' + ext
        if self.title in os.listdir():
            print('File already exists...')
        else:
            fname = open(self.title, 'wt')
            fname.close()
    
    def write_data(self, data):
        """
        Append existing file
        """
        with open(self.title, 'a') as rfile:
            rfile.write(data)

    def read_counter(self):
        if path.exists('counter.json'):
            return loads(open('counter.json'), 'r') + 1
    
    def write_counter(self):
        with open('counter.json', 'w') as rfile:
            rfile.write(dumps(counter))