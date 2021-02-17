from django.db import models

from .views import _gref

class BaseModel(models.Model):
    reference = models.CharField(max_length = 100, unique=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.reference

    def __unicode__(self):
        return self.reference

    class Meta :
        abstract = True
