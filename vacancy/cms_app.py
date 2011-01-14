from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class VacancyApp(CMSApp):
    name = u"Vacancy"
    urls = ["vacancy.urls",]

apphook_pool.register(VacancyApp)
