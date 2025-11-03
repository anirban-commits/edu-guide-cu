from django.shortcuts import render
from .models import Subject

def home(request):
    est_subjects = Subject.objects.filter(exam_type='EST')
    return render(request, 'home.html', {'subjects': est_subjects})