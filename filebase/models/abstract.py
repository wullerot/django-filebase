from django.db import models
from django.utils.translation import ugettext_lazy as _


class Node(models.Model):

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created'),
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Modified'),
    )

    folder = models.ForeignKey(
        'filebase.Folder',
        null=True,
        default=None,
        blank=True,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_set',
        verbose_name=_('Folder')
    )

    class Meta:
        abstract = True
