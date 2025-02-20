import json
import shutil
import os
import sys

import regex as re

class Convertor(): #TODO
    def __init__(self):
        pass
    
    def description_file_parser(self, file): #TODO
        with open(file, 'r') as f:
            data = json.load(f)
        return data

    def file_tree_crawler(self, path): #TODO
        pass


if __name__ == "__main__": #TODO
    print("Not yet implemented")