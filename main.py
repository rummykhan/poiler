from routes.Router import Router
from controllers.AppController import AppController


def start_main():
    arguments = Router().parse_routes()

    verbose = bool(arguments.verbose)

    if arguments.app:
        (AppController(verbose=verbose)).run()


if __name__ == '__main__':
    start_main()
