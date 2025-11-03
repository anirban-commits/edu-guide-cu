from django.shortcuts import render
from .models import Subject

def home(request):
    est_subjects = Subject.objects.filter(exam_type='EST')
    return render(request, 'home.html', {'subjects': est_subjects})

from django.shortcuts import render, get_object_or_404
from .models import Subject

def home(request):
    est_subjects = Subject.objects.filter(exam_type='EST')
    return render(request, 'home.html', {'subjects': est_subjects})

def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    return render(request, 'subject_detail.html', {'subject': subject})