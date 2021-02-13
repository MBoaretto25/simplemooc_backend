from django.shortcuts import render
from .models import Course


def index(request):
    return render(request, "courses/index.html", {"courses": Course.object.all()})


def details(request, pk):
    course = Course.object.get(pk=pk)
    context = {
        'course': course
    }
    template_name = 'courses/details.html'
    return render(request, template_name, context)
