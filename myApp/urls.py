from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.proj_list, name='projects'),
    path('activities/', views.act_list, name='activities'),
    path('future/', views.future, name='future'),

    #path('proj_detail/<slug:proj_title>', views.proj_detail, name='proj_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
