import argparse


class Parser(object):
    parser = None

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Basic Boiler Plate for Console Apps")
        self.parser.add_argument('-v', '--verbose', action='store_true')
