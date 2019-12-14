from django.db import models
from django.utils.translation import ugettext_lazy as _

from .abstract import Node


class Folder(Node):

    name = models.CharField(
        max_length=50,
        verbose_name=_('name'),
    )

    class Meta:
        abstract = False
        ordering = ['name']
        verbose_name = _('Folder')
        verbose_name_plural = _('Folders')

    def __str__(self):
        return '{}'.format(self.name)

    def get_folders(self):
        return self.filebase_folder_set.all()

    def get_files(self):
        return self.filebase_file_set.all()
