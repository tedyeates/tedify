from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Genre(models.Model):

    name = models.CharField(_("Genre Name"), max_length=50)
    description = models.CharField(_("Genre Description"), max_length=100)

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __str__(self):
        return self.name
