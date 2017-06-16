import argparse
from config.config import Config

r""" Useless Wrapper over Parser

For now This is a useless wrapper over argparse, But I'll make something useful out of it.

"""

class Parser(object):
    parser = None

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=Config.get('app_name'))
        self.parser.add_argument('-v', '--verbose', action='store_true')
