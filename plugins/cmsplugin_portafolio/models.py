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
    service = models.ForeignKey(Service, related_name="proyectos")
    country = CountryField()
    client = models.ForeignKey(Client, related_name ="proyectos")
    name = models.CharField(max_length= 100)
    description_short = models.TextField()
    description_long  = models.TextField()
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.name
class Image(models.Model):
    image = models.ImageField(upload_to= "uploaded_images")
    proyect = models.ForeignKey(Proyect, related_name="images")

class ProyectPlugin(CMSPlugin):
    portafolio = models.ManyToManyField(Proyect)


