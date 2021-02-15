from django.shortcuts import render, get_object_or_404
from .models import Course


def index(request):
    return render(request, "courses/index.html", {"courses": Course.object.all()})


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course
    }
    template_name = 'courses/details.html'
    return render(request, template_name, context)
