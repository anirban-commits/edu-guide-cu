from django.contrib import admin
from .models import Subject, Resource

class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 1  # Shows one blank form by default

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'exam_type']
    inlines = [ResourceInline]

admin.site.register(Resource)