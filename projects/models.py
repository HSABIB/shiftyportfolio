from django.db import models

from core.models import BaseModel

from core.views import _gref

class Category(BaseModel):
    number = models.IntegerField(default=0)
    label = models.CharField(max_length = 150)
  
    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random = _gref(5)
            if Category.objects.filter(reference=random).exists():
                continue
            self.reference = random
            break
        return self.reference
    
    def save(self, *args, **kwargs):
        if self.pk is None :
            self.generate()
        super(Category, self).save(*args, **kwargs)

class Project(BaseModel):
    flabel = models.CharField(max_length = 150)
    llabel = models.CharField(max_length = 150)
    miniature = models.TextField(default="")
    slogan = models.CharField(max_length = 150)
    creator = models.CharField(max_length = 150)
    project_details = models.TextField(default="") # text field

    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random = _gref(5)
            if Project.objects.filter(reference=random).exists():
                continue
            self.reference = random
            break
        return self.reference
    
    def save(self, *args, **kwargs):
        if self.pk is None :
            self.generate()
        super(Project, self).save(*args, **kwargs)

    def get_categories(self):
        categories = []
        for project_category in ProjectCategory.objects.filter(project=self):
            categories.append(project_category.category)
        return categories

class ProjectCategory(BaseModel):
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    category = models.ForeignKey('projects.Category', on_delete=models.CASCADE)
   
    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random = _gref(5)
            if ProjectCategory.objects.filter(reference=random).exists():
                continue
            self.reference = random
            break
        return self.reference
    
    def save(self, *args, **kwargs):
        if self.pk is None :
            self.generate()
        super(ProjectCategory, self).save(*args, **kwargs)
