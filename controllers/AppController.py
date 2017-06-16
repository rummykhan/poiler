from controllers.Controller import Controller


class AppController(Controller):
    def run(self):
        self.logger.log('App Running')
