from django.db import models

from core.models import BaseModel
from core.utils import generate_reference

class Project(BaseModel):
    miniature   = models.TextField(default="")
    main_miniature   = models.TextField(default="")
    slogan      = models.CharField(max_length = 150)
    body        = models.TextField(blank=True, null=True) # text field
    tech_body   = models.TextField(blank=True, null=True) # text field
    price       = models.FloatField(default=0.00)

    def __str__(self):
        return self.reference

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.reference = generate_reference(Project, 10)
        super(Project, self).save(*args, **kwargs)
