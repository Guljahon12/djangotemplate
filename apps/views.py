from django.shortcuts import render

# Create your views here.
from apps.models import Jobs


def index(request):
    jobs = Jobs.objects.all()
    context = {
        'jobs': jobs
    }
    return render(request, 'index.html', context)
