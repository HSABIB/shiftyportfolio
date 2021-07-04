from django.contrib import admin
from projects.models import *

class ProjectAdmin(admin.ModelAdmin):
    
    list_display = ['reference', 'slogan', 'price', 'deleted']

class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ['reference', 'label']

class ProjectCategoryAdmin(admin.ModelAdmin):

    list_display = ['reference', 'project', 'category']
    list_filter  = ['project', 'category']

class ServiceAdmin(admin.ModelAdmin):

    list_display = ['reference', 'label', 'icon']

class SubServiceAdmin(admin.ModelAdmin):

    list_display = ['reference', 'label', 'service']
    list_filter = ['service']

class SubServiceTechnologyAdmin(admin.ModelAdmin):

    list_display = ['reference', 'label', 'sub_service']
    list_filter = ['sub_service']

class ChapterAdmin(admin.ModelAdmin):

    list_display = ['reference', 'index', 'deleted']

class SubServiceChapterContentAdmin(admin.ModelAdmin):

    list_display = ['reference', 'chapter', 'sub_service']
    list_filter = ['chapter', 'sub_service']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SubService, SubServiceAdmin)
admin.site.register(SubServiceTechnology, SubServiceTechnologyAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(SubServiceChapterContent, SubServiceChapterContentAdmin)
