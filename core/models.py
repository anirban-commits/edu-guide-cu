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
class Resource(models.Model):
    RESOURCE_TYPE_CHOICES = [
        ('video', 'YouTube Video'),
        ('pdf', 'PDF Notes'),
    ]
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='resources')
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPE_CHOICES)
    title = models.CharField(max_length=200)
    # For YouTube: store video ID (e.g., dQw4w9WgXcQ)
    # For PDF: store filename (we'll handle uploads later)
    video_id = models.CharField(max_length=50, blank=True, help_text="YouTube video ID (e.g., dQw4w9WgXcQ)")
    pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} ({self.get_resource_type_display()}) for {self.subject.name}"
    
    def get_embed_url(self):
        if self.resource_type == 'video' and self.video_id:
            return f"https://www.youtube.com/embed/{self.video_id}"
        return None