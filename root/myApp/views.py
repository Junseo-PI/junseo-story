from django.shortcuts import render, HttpResponse, get_object_or_404
from django.shortcuts import redirect

from .models import Project, Activity, Future, en_Project, en_Activity, en_Future

# Create your views here.
def index(request):
    return render(request, 'kr/index.html')

def en_index(request):
    return render(request, 'en/index.html')

def redirect_url(request):
    response = redirect('/kr/')
    return response

# 1) projects
def proj_list(request):
    proj_list = Project.objects.all()
    context = {'proj_list' : proj_list}
    return render(
        request,
        'kr/projects.html',
        context
    )

# 2) activities
def act_list(request):
    act_list = Activity.objects.all()
    context = {'act_list' : act_list}
    return render(
        request,
        'kr/activities.html',
        context
    )

# 3) Future
def future(request):
    future_list = Future.objects.all()
    context = {'future_list' : future_list}
    return render(
        request,
        'kr/future.html',
        context
    )



# 1) projects
def en_proj_list(request):
    en_proj_list = en_Project.objects.all()
    context = {'en_proj_list' : en_proj_list}
    return render(
        request,
        'en/projects.html',
        context
    )

# 2) activities
def en_act_list(request):
    en_act_list = en_Activity.objects.all()
    context = {'en_act_list' : en_act_list}
    return render(
        request,
        'en/activities.html',
        context
    )

# 3) Future
def en_future(request):
    en_future_list = en_Future.objects.all()
    context = {'en_future_list' : en_future_list}
    return render(
        request,
        'en/future.html',
        context
    )
