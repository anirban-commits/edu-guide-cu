from django.db import models

class Subject(models.Model):
    EXAM_CHOICES = [
        ('MST-1', 'MST-1'),
        ('MST-2', 'MST-2'),
        ('EST', 'End Semester'),
    ]
    
    name = models.CharField(max_length=100)
    exam_type = models.CharField(max_length=10, choices=EXAM_CHOICES)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.exam_type})"