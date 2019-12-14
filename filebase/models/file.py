from django.db import models
from django.utils.translation import ugettext_lazy as _

from easy_thumbnails.fields import ThumbnailerField

from .. import conf
from .abstract import Node


class File(Node):

    file = ThumbnailerField(
        upload_to=conf.UPLOAD_TO,
        storage=conf.FILE_STORAGE,
        thumbnail_storage=conf.THUMBNAIL_STORAGE,
        verbose_name=_('File'),
    )
    file_name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name=_('File name'),
        help_text=_('Used for renaming your file on the server'),
    )

    class Meta:
        abstract = False
        ordering = ['name']
        verbose_name = _('File')
        verbose_name_plural = _('File')

    def __str__(self):
        return '{}'.format(self.name)
