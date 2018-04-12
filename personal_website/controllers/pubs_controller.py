import pyramid_handlers
from personal_website.controllers.base_controller import BaseController


class PublicationsController(BaseController):
    @pyramid_handlers.action(renderer='templates/publications/index.pt')
    def index(self):
        return {'value': 'PUBLICATIONS'}
