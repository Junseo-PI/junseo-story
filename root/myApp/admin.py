from django.contrib import admin
from .models import Project, Activity, Future, en_Project, en_Future, en_Activity

# Register your models here.
admin.site.register(Project)
admin.site.register(Activity)
admin.site.register(Future)
admin.site.register(en_Project)
admin.site.register(en_Activity)
admin.site.register(en_Future)
