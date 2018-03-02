# -*- coding: utf-8 -*-
from django.db import models
from django.utils import translation


class DocumentManager(models.Manager):
    def ___instances___(self, request):
        instances = self.all()
        instances___position_not_equal_0 = instances.exclude(position__lte=0)
        instances___position_equal_0 = instances.exclude(position__gt=0)
        int___position = 1
        if instances___position_not_equal_0.count() > 0:
            for instance in instances___position_not_equal_0:
                instance.position = int___position
                instance.save()
                int___position += 1
        if instances___position_equal_0.count() > 0:
            for instance in instances___position_equal_0:
                instance.position = int___position
                instance.save()
                int___position += 1
        instances = self.all()
        return instances

    def ___instance___(self, request, pk):
        try:
            instance = self.get(pk=pk)
        except Document.DoesNotExist:
            return None
        return instance

    def ___instance___by_pk___(self, pk):
        try:
            instance = self.get(pk=pk)
        except Document.DoesNotExist:
            return None
        return instance


class Document(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        editable=True,
    )
    modified = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        editable=True,
    )
    title_en = models.CharField(
        default='',
        max_length=1024,
        null=True,
        blank=True,
    )
    title_es = models.CharField(
        default='',
        max_length=1024,
        null=True,
        blank=True,
    )
    content_en = models.TextField(
        default='',
        null=True,
        blank=True,
    )
    content_es = models.TextField(
        default='',
        null=True,
        blank=True,
    )
    parent = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True,
    )
    position = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True,
    )
    objects = DocumentManager()

    class Meta:
        db_table = 'application___help___document'
        ordering = ['position', 'id', ]

    def __str__(self):
        if translation.get_language() == 'en':
            return '%(title)s' % {'title': self.title_en, }
        elif translation.get_language() == 'es':
            return '%(title)s' % {'title': self.title_es, }
        else:
            return '%(id)s' % {'id': self.id, }

    def ___string___content___(self):
        if translation.get_language() == 'en':
            return '%(content)s' % {'content': self.content_en, }
        elif translation.get_language() == 'es':
            return '%(content)s' % {'content': self.content_es, }
        else:
            return '%(content)s' % {'content': '', }
