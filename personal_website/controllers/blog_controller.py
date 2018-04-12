import pyramid_handlers
from personal_website.controllers.base_controller import BaseController


class BlogController(BaseController):
    @pyramid_handlers.action(renderer='templates/blog/index.pt')
    def index(self):
        # data / service access
        # return model
        return {'value': 'BLOG'}

    @pyramid_handlers.action(renderer='templates/blog/plumed_net.pt')
    def plumed_net(self):
        # data / service access
        # return model
        return {'value': 'PLUMED_NET'}

    @pyramid_handlers.action(renderer='templates/blog/post2.pt')
    def post2(self):
        # data / service access
        # return model
        return {'value': 'POST2'}

    @pyramid_handlers.action(renderer='templates/blog/post3.pt')
    def post3(self):
        # data / service access
        # return model
        return {'value': 'POST3'}
