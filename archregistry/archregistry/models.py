from django.db import models


class ArchUser(models.Model):

    """ A simple user model for the Arch hipsters. """

    name = models.CharField(max_length=250)
    nick = models.CharField('nick (IRC)', max_length=250)
    link = models.URLField()

    def __unicode__(self):
        return self.name

    class Meta():
        ordering = ['name']
