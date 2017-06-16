from controllers.Controller import Controller


class AppController(Controller):
    def run(self):
        self.logger.info('App Running')
