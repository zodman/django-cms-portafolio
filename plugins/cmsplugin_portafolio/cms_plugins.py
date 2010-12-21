from plugins.cmsplugin_portafolio.models import PortafolioPlugin
from cms.plugin_pool import plugin_pool
from cms.models import CMSPluginBase

class PortafolioPlugin(CMSPluginBase):
    model = PortafolioPlugin
    render_template = 'portafolio/portafolio.html'
    name = "Portafolio"

    def render(self, context, instance, placeholder):
        context.update({'instance':instance,'placeholder':placeholder})
        return context

plugin_pool.register_plugin(PortafolioPlugin)
