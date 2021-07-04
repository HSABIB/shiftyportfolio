from django.db import models

from core.models import BaseModel
from core.utils import generate_reference

class Category(BaseModel):
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.reference = generate_reference(Category, 10)
        super(Category, self).save(*args, **kwargs)

class Project(BaseModel):
    miniature       = models.TextField(default="")
    scaled          = models.TextField(default="")
    main_miniature  = models.TextField(default="")
    slogan          = models.CharField(max_length = 150)
    body            = models.TextField(blank=True, null=True) # text field
    tech_body       = models.TextField(blank=True, null=True) # text field
    price           = models.FloatField(default=0.00)

    def __str__(self):
        return self.slogan

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.reference = generate_reference(Project, 10)
        super(Project, self).save(*args, **kwargs)

    def get_scaled_miniature(self) :
        list_url =  self.miniature.split('/')
        list_url.insert(6, 'c_scale,h_350')
        return '/'.join(list_url)

    def get_categories(self):
        categories_list = []
        for temp in ProjectCategory.objects.filter(project=self) :
            categories_list.append( temp.category )
        return categories_list

class ProjectCategory(BaseModel):
    category    = models.ForeignKey("projects.Category", on_delete=models.CASCADE) 
    project     = models.ForeignKey("projects.Project", on_delete=models.CASCADE) 

    def __str__(self):
        return self.reference

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.reference = generate_reference(ProjectCategory, 15)
        super(ProjectCategory, self).save(*args, **kwargs)

class Service(BaseModel):
    label = models.CharField(max_length=255)
    small_desc = models.TextField(default="")
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.label

    def get_sub_services(self):
        return SubService.objects.filter(service=self)

class SubService(BaseModel):
    service = models.ForeignKey("projects.Service", on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    slogan = models.CharField(max_length=255)
    small_desc = models.TextField(default="")
    big_desc = models.TextField(default="")
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.reference

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.reference = generate_reference(SubService, 10)
        super(SubService, self).save(*args, **kwargs)

class SubServiceTechnology(BaseModel):
    sub_service = models.ForeignKey("projects.SubService", on_delete=models.CASCADE)
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.reference = generate_reference(SubServiceTechnology, 15)
        super(SubServiceTechnology, self).save(*args, **kwargs)

class Chapter(BaseModel):
    miniature = models.TextField(default="")
    index = models.IntegerField(default=1)

    def __str__(self):
        return self.reference

class SubServiceChapterContent(BaseModel):
    sub_service = models.ForeignKey("projects.SubService", on_delete=models.CASCADE)
    chapter = models.ForeignKey("projects.Chapter", on_delete=models.CASCADE)
    content = models.TextField(default="")

    def __str__(self):
        return self.reference

    def save(self, *args, **kwargs):
        if self.pk is None :
            self.reference = generate_reference(SubServiceChapterContent, 15)
        super(SubServiceChapterContent, self).save(*args, **kwargs)

