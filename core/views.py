from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Subject

def home(request):
    query = request.GET.get('q')
    if query:
        subjects = Subject.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query),
            exam_type='EST'  # ← You’re using EST, not MST-1
        )
    else:
        subjects = Subject.objects.filter(exam_type='EST')
    return render(request, 'home.html', {'subjects': subjects, 'query': query})

def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    return render(request, 'subject_detail.html', {'subject': subject})