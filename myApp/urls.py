from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.redirect_url, name='index'),
    path('kr/', views.index, name='index'),
    path('kr/projects/', views.proj_list, name='projects'),
    path('kr/activities/', views.act_list, name='activities'),
    path('kr/future/', views.future, name='future'),

    path('en/', views.en_index, name='en_index'),
    path('en/projects/', views.en_proj_list, name='en_projects'),
    path('en/activities/', views.en_act_list, name='en_activities'),
    path('en/future/', views.en_future, name='en_future'),

    #path('proj_detail/<slug:proj_title>', views.proj_detail, name='proj_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
