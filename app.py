from wsgiref.simple_server import make_server
from tg import expose, TGController, MinimalApplicationConfigurator
import webhelpers2
import webhelpers2.text
from tg.configurator.components.statics import StaticsConfigurationComponent


# RootController of our web app, in charge of serving content for /
class RootController(TGController):

    @expose('public.index')
    def index(self):
        return dict()

# Configure a new minimal application with our root controller.

config = MinimalApplicationConfigurator()
config.register(StaticsConfigurationComponent)
config.update_blueprint({
    'root_controller': RootController(),
    'renderers': ['kajiki'],
    'helpers': webhelpers2,
    'serve_static': True,
    'paths': {
        'static_files': 'public'
    }
})
# Serve the newly configured web application.
print("Serving on port 8080...")
httpd = make_server('', 8080, config.make_wsgi_app())
httpd.serve_forever()