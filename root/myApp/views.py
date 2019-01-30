from django.shortcuts import render, HttpResponse, get_object_or_404
from django.shortcuts import redirect

from .models import Project, Activity, Future

# Create your views here.
def index(request):
    return render(request, 'index.html')


# 1) projects
def proj_list(request):
    proj_list = Project.objects.all()
    context = {'proj_list' : proj_list}
    return render(
        request,
        'projects.html',
        context
    )

# 2) activities
def act_list(request):
    act_list = Activity.objects.all()
    context = {'act_list' : act_list}
    return render(
        request,
        'activities.html',
        context
    )

# 3) Future
def future(request):
    future_list = Future.objects.all()
    context = {'future_list' : future_list}
    return render(
        request,
        'future.html',
        context
    )
