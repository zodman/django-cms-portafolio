from django.db import models



class Candidate(models.Model):
    name = models.CharField(max_length=200, unique = True)
    email = models.EmailField(unique  = True )
    phone = models.CharField(max_length=15)
    cv = models.FileField(upload_to = "photos/%Y/%m/%d/")
    opening = models.ForeignKey("EnableOpening", related_name="candidates")

    def __unicode__(self):
        return self.name

class Require(models.Model):
    description = models.TextField()
    def __unicode__(self):
        return self.description

class Opening(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    require = models.ForeignKey(Require, related_name="openings")
    slug = models.SlugField()
    @models.permalink
    def get_absolute_url(self):
        return ("job-detail", [self.slug] )
    def __unicode__(self):
        return self.title

class EnableOpening(models.Model):
    opening = models.ForeignKey(Opening)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.opening.title

