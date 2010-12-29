from django.db import models
from django_countries import CountryField
from cms.models import CMSPlugin

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
class Client(models.Model):
    name = models.CharField(max_length= 100)

    def __unicode__(self):
        return self.name

class Proyect(models.Model):
    service = models.ForeignKey(Service, related_name="proyects")
    country = CountryField()
    client = models.ForeignKey(Client, related_name ="proyects")
    name = models.CharField(max_length= 100)
    description_short = models.TextField()
    description_long  = models.TextField()
    url = models.URLField(blank=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name
class Image(models.Model):
    image = models.ImageField(upload_to= "uploaded_images")
    main = models.BooleanField(default =False)
    proyect = models.ForeignKey(Proyect, related_name="images")

class PortafolioPlugin(CMSPlugin):
    portafolio = models.ManyToManyField(Proyect)


