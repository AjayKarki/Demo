from django.db import models


class BlogQuerySet(models.QuerySet):

    def published(self):
        return self.filter(published=True)


class BlogManager(models.Manager):
    def get_queryset(self):
        return BlogQuerySet(self.model, using=self._db)  # Important!

    def published(self):
        return self.get_queryset().published()

