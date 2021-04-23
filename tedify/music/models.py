from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Genre(models.Model):

    name = models.CharField(_("Genre Name"), max_length=10, unique=True)
    description = models.CharField(_("Genre Description"), max_length=100)

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __str__(self):
        return self.name

class Artist(models.Model):

    name = models.CharField(_("Artist Name"), max_length=10)
    description = models.CharField(_("Artist Description"), max_length=100)
    age = models.PositiveSmallIntegerField(_("Artist Age"))
    genres = models.ManyToManyField(Genre, verbose_name=_("Artist Genres"))

    class Meta:
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")

    def __str__(self):
        return self.name
