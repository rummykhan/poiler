from base.support.parser import Parser


class Router(Parser):
    def __init__(self):
        super().__init__()
        self.boot()

    def boot(self):
        self.parser.add_argument('-a', '--app', action='store_true')

    def parse_routes(self, args=None, namespace=None):
        return self.parser.parse_args(args=args, namespace=namespace)
